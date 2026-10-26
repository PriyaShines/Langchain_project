from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Recipe(BaseModel):
    recipies: list


@app.post("/api/generate_recipe")
def generate_recipe(recipe: Recipe):
    return {"message": "Recipe generated successfully using incredients: " + ", ".join(recipe.recipies) }
