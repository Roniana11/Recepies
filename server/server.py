from unittest import result
from fastapi import FastAPI,HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from typing import Union

from utils.utils import filter_recipes_by_ingridient,format_results
from services.ingredient_api import get_ingredients 
from services.recipes_api import fetch_recipes


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/{ingredient}',status_code=200)
async def get_recipes(ingredient,gluten: str,dairy: str):
    try:
        recipes = await fetch_recipes(ingredient)
        if gluten == "true":
            gluten_list = get_ingredients("gluten")
            recipes = filter_recipes_by_ingridient(gluten_list, recipes)
        if dairy == "true":
            dairy_list = get_ingredients("dairy")
            recipes = filter_recipes_by_ingridient(dairy_list, recipes)
        return format_results(recipes)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.args[0])
    except:
        raise HTTPException(status_code=500, detail="something went wrong")
if __name__ =="__main__":
      uvicorn.run(app, host="0.0.0.0", port=8000)

