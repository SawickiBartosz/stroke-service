from fastapi import FastAPI

app = FastAPI()

@app.get("/stroke_proba")
def predict_proba():
    return {'probability' : 1}
    
    
@app.get("/")
def hello_world():
    return "Hello World"
