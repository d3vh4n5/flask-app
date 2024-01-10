

export function addItemList(divContent, itemText="", template = "<h2> {{Item}} </h2>") {
    var item = template.replace("{{Item}}", itemText)

    divContent.innerHTML += item;
    divContent.innerHTML += "<br>";
}