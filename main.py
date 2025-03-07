from symtable import Class
from urllib.request import Request

from fastapi import FastAPI
import pickle
import uvicorn
import sklearn
from pydantic import BaseModel

model = pickle.load(open("spam_model1_updated.pkl","rb"))
vectorizer = pickle.load(open("vectorize.pkl","rb"))




app = FastAPI()

class SMSRequest(BaseModel):
    message: str
@app.post("/predict/")
def predict(sms:SMSRequest):
    print(f"received: {sms}")
    transformed = vectorizer.transform([sms.message])
    prediction = model.predict(transformed)[0]


    result = "spam" if prediction == 1 else "ham"

    return {"message":sms.message, "prediction": result}


