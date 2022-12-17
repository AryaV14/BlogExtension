/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */

const btn = document.getElementById("btn")
btn.addEventListener("click", handleClick)

// innerHTML
function handleClick() {
  const textBox = document.getElementById("textbox")
  console.log(textbox.value)
 

}

function getOption() {
selectElement = document.querySelector('#cars');
output = selectElement.value;
console.log(output)
}