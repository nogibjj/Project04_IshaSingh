from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


@app.get('/')
async def index():
    return {"Real": "Python"}


tourist_attraction_db = [
    {
        'season': 'summer',
        'country': 'France',
        'cities': ['Paris','Lyon','Giriondinis'],
        'places': ['eifel_tower', 'cruise']
    }
]

class attractionfortourists_class(BaseModel):
    season: str
    country: str
    cities: List[str]
    places: List[str]


@app.get('/', response_model=List[attractionfortourists_class])
async def index():
    return tourist_attraction_db

@app.post('/', status_code=201)
async def add_movie(payload: attractionfortourists_class):
    attractions = payload.dict()
    tourist_attraction_db.append(attractions)
    return {'id': len(tourist_attraction_db) - 1}





