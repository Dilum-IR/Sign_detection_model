import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from tensorflow.keras.models import load_model

from Model.KeypointInput import KeypointInput
from Data.Actions import actions
from logger import logging

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load a model
model = load_model("train_model.h5")
logging.warning(str(model.summary()))


@app.get("/")
async def root():
    logging.info("request for root route")
    return {"message": "Hello Model"}


@app.post("/predict")
async def predict(sequence: KeypointInput):
    try:
        # print(sequence)
        logging.info("request for predictions")
        sequence = np.array(sequence.keypoint)

        # Assuming 1662 keypoint per frame
        if sequence.shape != (30, 1662):
            logging.error(str(e))
            raise HTTPException(status_code=400, detail="Invalid sequence shape")

        # Predict using the model
        res = model.predict(np.expand_dims(sequence, axis=0))[0]
        prediction = actions[np.argmax(res)] if res[np.argmax(res)] > 0.5 else "No confident prediction"
        
        # logging and pass response for users
        # Need to connect firebase realtime DB
        logging.info("model predict result:"+prediction)
        return {"prediction": prediction}

    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    logging.info("Starting Server app on http://127.0.0.1:9100")
    uvicorn.run("main:app", host="127.0.0.1", port=9100, reload=True)
