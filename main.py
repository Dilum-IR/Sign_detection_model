
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import uvicorn
# from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# model = load_model("./train_model.h5")

actions = ["hello", "thanks", "i love you"]


class KeypointInput(BaseModel):
    keypoint: List[List[float]]  # List of 30 frames, each containing flattened key points


@app.post("/predict")
async def predict(sequence: KeypointInput):
    try:
        # sequence = np.array(keypoint_input.sequence)

        print(sequence.keypoint)

        # if sequence.shape != (30, 1662):  # Assuming 1662 keypoint per frame
        #     raise HTTPException(status_code=400, detail="Invalid sequence shape")

        # Predict using the model
        # res = model.predict(np.expand_dims(sequence, axis=0))[0]
        # prediction = actions[np.argmax(res)] if res[np.argmax(res)] > 0.4 else "No confident prediction"

        return {"prediction": "prediction"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)
