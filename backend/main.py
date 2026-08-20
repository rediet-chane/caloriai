from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
from pydantic import BaseModel
from db import save_meal, get_todays_meals

from analysis import analyze_food

load_dotenv()

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/analyze")
async def analyze(image: UploadFile = File(...)):
    image_bytes = await image.read()

    result = analyze_food(image_bytes)

    return result
class MealSave(BaseModel):
    total_calories: int
    items: list


@app.post("/api/meals")
def save(meal: MealSave):
    save_meal(meal.total_calories, meal.items)
    return {"status": "saved"}


@app.get("/api/meals/today")
def todays_meals():
    return get_todays_meals()