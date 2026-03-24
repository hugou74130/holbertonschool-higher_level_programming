#!/usr/bin/node
document.querySelector("header").style.color = "#FF0000";
document.querySelector("#red_header").addEventListener("click", function() {
    document.querySelector("header").style.color = "#FF0000";
});
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then((response) => response.json())
    .then((data) => {
        document.querySelector("#character").textContent = data.name;
    })
    .catch((error) => {
        console.error("Error fetching character:", error);
    });