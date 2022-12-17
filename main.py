import joblib
import pandas as pd



#open pickle model

nationality_naive_bayes = open("/Users/isingh/Desktop/naive_bayes.pkl","rb")
nationality_cv = joblib.load(nationality_naive_bayes)


# import FastAPI
from fastapi import FastAPI


app = FastAPI()



# import uvicorn
import uvicorn


@app.get('/')
async def index():
  return {"text":"Our First route"}

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.0",port=8000)





