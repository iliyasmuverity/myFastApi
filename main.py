from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

db = []

class Friends(BaseModel):
    name: str
    city: str

@app.get('/friends')
def get_cities():
    results = []
    for you in db:
        results.append({'name' : you['name'], 'city': you['city']})
    return results

@app.post('/friends')
def create_you(you: Friends):
    db.append(you.dict())
    return db[-1]

