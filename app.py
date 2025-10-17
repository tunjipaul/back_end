from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

app = FastAPI(title = "My FastAPI Application", version = "1.0.0")

data = [
    {"name": "Sam Larry", "age": 20, "track": "AI Developer"},
    {"name": "Bahubili", "age": 21,"track": "Data Scientist"},
    {"name": "Walter White","age": 22, "track": "Backend Developer"},
]

class Item(BaseModel):
    name: str = Field(..., example= "Perpetual")
    age: int = Field(..., example = 25)
    track: str = Field(..., example = "Full Stack Developer")

@app.get("/", description="This endpoint just returns a welcome message")
def root():
    return {"message": "Welcome to My FastAPI Application!"}

@app.get("/get-data")
def get_data():
    return data

@app.post("/create-data")
def create_data(req: Item):
    data.append(req.dict())
    print(data)
    return {"message": "Data created successfully", "data": data}

if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
  