import { addItemList } from "./helper.js"

var myPlaceholder = document.getElementById("placeholder")

fetch('http://127.0.0.1:5000/productos')
    .then(response => response.json())
    .then(data => { 
        console.log(data)
        for (var product of data) {
            addItemList(myPlaceholder, product['name'])
        } 
    })