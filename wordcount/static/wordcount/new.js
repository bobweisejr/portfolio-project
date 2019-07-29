function checkInput(inputVal) {
//    var inputVal = document.getElementById();
 if (inputVal.value.length > inputVal.maxLength) inputVal.value = inputVal.value.slice(0, inputVal.maxLength);
}



function checkFilled2(inputVal) {

    if (inputVal.value > 1) {
        inputVal.style.backgroundColor = "yellow";
        inputVal.style.color = "black";
    }
    else{
        inputVal.style.backgroundColor = "";
    }
}
