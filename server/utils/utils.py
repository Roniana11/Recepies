def filter_recipes_by_ingridient(ingredients_list, recipes):
    mapped_ingredients = list(map(lambda ing: ing["name"],ingredients_list))
    filtered_recipes =[]
    for r in recipes:
        includes_ingredients = is_ingredients_intersect(r,mapped_ingredients)
        if not includes_ingredients:
            filtered_recipes.append(r)

    return filtered_recipes

def is_ingredients_intersect(recipe,ingredients):
    for ingredient in recipe["ingredients"]:
        for i in ingredients:
            if i in ingredient:
                return True

    return False


def format_results(results_list):
    return list(map(lambda r: {"idMeal": r["idMeal"],"ingredients": r["ingredients"],"title": r["title"],"thumbnail": r["thumbnail"],"strInstructions":r["strInstructions"], "href": r['href']},results_list))

