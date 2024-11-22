# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

# from firebase_functions import https_fn
# from firebase_admin import initialize_app

# initialize_app()

# import os
import stripe
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
# import numpy as np
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


# @https_fn.on_request()
# def on_request_test(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")


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


# This example sets up an endpoint using the Flask framework.
# Watch this video to get started: https://youtu.be/7Ul1vfmsDck.

# See your keys here: https://dashboard.stripe.com/apikeys
stripe.api_key = 'sk_test_51OXIY6SE8MZqjzvmoH00vOhSfKQiCrd8Ob14haVYbQclK18JJTgBEX9paKzRZ3dJ9SzdLa2bi4qhJPltKp0ESB9Y00IZwcuMrC'


@app.get('/payment-sheet')
async def payment_sheet():

    customer = stripe.Customer.create()
    ephemeralKey = stripe.EphemeralKey.create(
        customer=customer['id'],
        stripe_version='2024-11-20.acacia',
    )

    paymentIntent = stripe.PaymentIntent.create(
        amount=1099,  # $10.99
        currency='usd',
        customer=customer['id'],
        description='Payment for EchoLink subscription',
        automatic_payment_methods={
            'enabled': True,
        },
    )
    return {
            "paymentIntent": paymentIntent.client_secret,
            "ephemeralKey": ephemeralKey.secret,
            "customer": customer.id,
            "publishableKey": 'pk_test_51OXIY6SE8MZqjzvm9EuoCGVCtkJGQxbcfxDxxJZ3ev7xvtTCUePz6liBSlMSMqibkvdbbxrccYlyrCixzUerS2SY00pEyJFQ0e'
            }


if __name__ == "__main__":
    # port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)
