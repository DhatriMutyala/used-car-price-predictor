let brandModelMap = JSON.parse(document.getElementById("data").textContent);

function loadBrands(){
let brandDropdown = document.getElementById("brand");

for(let brand in brandModelMap){
let option = document.createElement("option");
option.value = brand;
option.text = brand;
brandDropdown.appendChild(option);
}
}

function updateModels(){
let brand = document.getElementById("brand").value;
let modelDropdown = document.getElementById("model");

modelDropdown.innerHTML = "";

if(brandModelMap[brand]){
brandModelMap[brand].forEach(function(model){
let option = document.createElement("option");
option.value = model;
option.text = model;
modelDropdown.appendChild(option);
});
}
}

document.getElementById("brand").addEventListener("change", updateModels);

window.onload = function(){
loadBrands();
updateModels();
};