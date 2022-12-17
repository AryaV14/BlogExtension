/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */

  const btn = document.getElementById("btn")
  btn.addEventListener("click", handleClick)

// innerHTML
function handleClick() {
    const textBox = document.getElementById("textbox")
    console.log(textbox.value)
   

}
function show(value) {
    console.log(value)
    document.querySelector(".text-box").value = value;

  }
  
  let dropdown = document.querySelector(".dropdown")
  dropdown.onclick = function() {
      dropdown.classList.toggle("active")
  }