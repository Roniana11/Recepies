const renderer = new RecipesRenderer();
const recipes = new Recepies();

async function renderRecipes() {
  const ingredientName = $("#recipe-input").val();
  const glutenFree =$( "#gluten-input").is(":checked");
  const dairyFree = $("#dairy-input").is(":checked");

  try {
    await recipes.loadRecipes(ingredientName, glutenFree, dairyFree);
    renderer.reRender(recipes.getRecipes());
  } catch (e) {
    if (e.status === 404) {
      renderer.renderModal("error", "There is no such ingredient");
    } else {
      renderer.renderModal("error", "oooops! we had a problem");
    }
  }
}

async function showInstructionsHandler(elemnt) {
  const id = $(elemnt).closest(".recipe-container").attr("id");
  const recepieInstructions = recipes.getRecipeInstruction(id);
  renderer.renderModal("Instructions", recepieInstructions);
}

function alertsIngredientHandler(element){
  const firstIngredient = $(element).closest(".recipe-container").find(".ingredients-list").children(":first").text()
  alert(firstIngredient);
}

$("#serach-btn").on("click", renderRecipes);

$("#recipes-container").on("click", ".img-container", ({ target }) =>
alertsIngredientHandler(target)
)


$("#recipes-container").on("click", ".instructions-btn", ({ target }) =>
  showInstructionsHandler(target)
);

$("#demo-modal").on("click", ".close-btn", renderer.removeModal);
