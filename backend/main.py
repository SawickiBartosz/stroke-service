from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
	"https://spages.mini.pw.edu.pl/~sawickib/stroke-prediction/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/stroke_proba")
def predict_proba():
    return {'probability' : 1}
    
    
@app.get("/")
def hello_world():
    return "Hello World"
