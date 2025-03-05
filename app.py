from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Walmart Product Recommender!"}

@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: str):
    with open("precomputed_recommendations.json", "r", encoding="utf-8") as f:
        recommendations = json.load(f)
    return recommendations.get(user_id, [])
