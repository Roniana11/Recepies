import json
import requests

URL = 'https://recipes-goodness.herokuapp.com/recipes/'

async def fetch_recipes(ingredient):
    res = requests.get(url= URL + ingredient)
    result = res.json()["results"]
    if not result:
        raise Exception("There are no recipes for that specific ingredient")
    return result
