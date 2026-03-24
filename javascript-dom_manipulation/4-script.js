#!/usr/bin/node
document.querySelector("header").style.color = "#FF0000";
document.getElementById("add_item").addEventListener("click", function() {
    const newItem = document.createElement("li");
    newItem.textContent = "Item";
    document.querySelector(".my_list").appendChild(newItem);
});