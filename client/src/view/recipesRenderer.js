class RecipesRenderer {
  reRender(recipes) {
    const container = $("#recipes-container");
    container.empty();
    let newRecepiesEl = this.createTemplateEl("recipe-template", {recipes});
    container.append(newRecepiesEl);
  }

  renderModal(title, content) {
    const container = $("#demo-modal");
    container.css("display", "flex");
    let newModalEl = this.createTemplateEl("modal-template", {
      title,
      content,
    });

    container.append(newModalEl);
  }

  removeModal() {
    const container = $("#demo-modal");
    container.css("display", "none");
    container.empty();
  }

  createTemplateEl(id, data) {
    let source = $(`#${id}`).html();
    let template = Handlebars.compile(source);
    let newEl = template(data);
    return newEl;
  }
}
