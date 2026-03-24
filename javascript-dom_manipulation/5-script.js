document.querySelector("header").style.color = "#FF0000";
document.getElementById("update_header").addEventListener("click", function() {
    document.querySelector("header").textContent = "New Header!!!";
});