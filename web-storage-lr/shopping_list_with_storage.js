window.addEventListener("load", setup);

function setup() {
    addListeners();
    const data = retrieveItemsFromLocalStorage();
    populateShoppingList(data);
}

function addListeners() {
    document.getElementById("addNewItemButton").addEventListener("click", addNewItem);
    document.getElementById("deleteSelectedItemsButton").addEventListener("click", deleteSelectedItems);
    document.getElementById("selectAllItemsButton").addEventListener("click", selectAllItems);
}

function retrieveItemsFromLocalStorage() {
    const data = [];
    for (let i = 0; i < localStorage.length; i++){
        const key = localStorage.key(i);
        const value = localStorage.getItem(key);
        const item = {};
        item[key] = value;
        data.push(item);
    }
    return data;
}

function populateShoppingList(data) {
    for (const datum of data) {
        for (const [key, value] of Object.entries(datum)){
            addItemToShoppingListArea(key, value);
        }
    }
}

function addItemToShoppingListArea(key, value){
    const divElement = document.createElement("div");
    const listItemCheckBoxElement = document.createElement("input");
    listItemCheckBoxElement.setAttribute("type", "checkbox");
    listItemCheckBoxElement.setAttribute("name", "checkBoxName");
    listItemCheckBoxElement.setAttribute("class", "checkBoxClass");
    const checkBoxLabelElement = document.createElement("label");
    checkBoxLabelElement.setAttribute("for", "checkBoxName");
    checkBoxLabelElement.textContent = `${key} - ${value}`;
    listItemCheckBoxElement.setAttribute("id", key);
    const breakElement = document.createElement("br");
    divElement.appendChild(listItemCheckBoxElement);
    divElement.appendChild(checkBoxLabelElement);
    divElement.appendChild(breakElement);
    const listDivElement = document.getElementById("listOfItems");
    listDivElement.appendChild(divElement);
}

function addNewItem(){
    const divElement = document.createElement("div");
    const itemInputTextElement = document.createElement("input");
    itemInputTextElement.setAttribute("type", "text");
    itemInputTextElement.setAttribute("size", 15);
    itemInputTextElement.setAttribute("id", "newItemDescription");
    const quantityInputTextElement = document.createElement("input");
    quantityInputTextElement.setAttribute("type", "text");
    quantityInputTextElement.setAttribute("size", 15);
    quantityInputTextElement.setAttribute("id", "newItemQuantity");
    const addNewButton = document.createElement("input");
    addNewButton.setAttribute("type", "button");
    addNewButton.setAttribute("id", "addNewButtonID");
    addNewButton.setAttribute("value", "Add New Item");
    addNewButton.addEventListener("click", addNewItemToTheShoppingList);
    const itemListDiv = document.getElementById("inputForNewItem");
    itemListDiv.appendChild(itemInputTextElement);
    itemListDiv.appendChild(quantityInputTextElement);
    itemListDiv.appendChild(addNewButton);
}

function addNewItemToTheShoppingList(){
    const itemTextDescriptionElement = document.getElementById("newItemDescription");
    const quantityInputTextElement = document.getElementById("newItemQuantity");
    const itemKey = itemTextDescriptionElement.value;
    const itemValue = quantityInputTextElement.value;
    addItemToShoppingListArea(itemKey, itemValue);
    const itemListDiv = document.getElementById("inputForNewItem");
    itemListDiv.removeChild(itemTextDescriptionElement);
    itemListDiv.removeChild(quantityInputTextElement);
    itemListDiv.removeChild(document.getElementById("addNewButtonID"));
    localStorage.setItem(itemKey, itemValue);
}

function selectAllItems(){
    const checkBoxList = document.getElementsByClassName("checkBoxClass");
    for (let i = 0; i < checkBoxList.length; i++) {
        checkBoxList[i].checked = true;
    }
}

function deleteSelectedItems(){
    const checkBoxList = document.getElementsByClassName("checkBoxClass");
    for (let i = checkBoxList.length - 1; i >= 0; i--) {
        if (checkBoxList[i].checked === true) {
            localStorage.removeItem(checkBoxList[i].id);
            checkBoxList[i].parentElement.remove();
        }
    }
}
