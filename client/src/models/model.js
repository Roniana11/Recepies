class Recepies {

  #recipes = [];


  getRecipes() {
    // return JSON.parse(JSON.stringify(this.#recipes))
    return this.#recipes;
  }

  cleanRecipes() {
    this.#recipes.length = 0;
  }

  getRecipeInstruction(id) {
    const recepie = this.#recipes.find((r) => r.idMeal === id);
    return recepie.strInstructions;
  }

  async loadRecipes(ingredient, gluten, dairy) {
    const data = await fetchRecipes(ingredient, gluten, dairy);
    this.cleanRecipes();
    this.#recipes = data;
  }
}
