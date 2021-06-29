const task3Element = document.getElementById('task-3');

function showAlert(){
    alert("This is an alert!")
}

function nameAlert(name){
    alert("Hello im " +name)
}

function joinStrings(one, two, three){
    return one + two + three
}

//showAlert()
nameAlert("SpongeBob")
task3Element.addEventListener("click", showAlert)
alert(joinStrings("Pepe", "Pela", "Papas"))

