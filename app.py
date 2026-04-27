from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Enterprise AI Assistant Running"
    }

@app.get("/predict")
def predict():
    return {
        "prediction":"Estimated next month cost: 165000"
    }
