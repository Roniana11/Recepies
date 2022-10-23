async function fetchRecipes(ingredient,gluten,dairy) {
  let URL = `http://localhost:8000/${ingredient}?gluten=${gluten}&dairy=${dairy}`;
  const data = await $.get(URL, {
    headers: { "Access-Control-Allow-Origin": "*" },
  });
  return data;
}

