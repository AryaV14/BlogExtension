
    
    var barChartData = {
        labels: [
         "TRAVEL","FOOD","TECH","MUSIC"
        ],
        datasets: [
          {
            label: "READ",
            backgroundColor: "lightred",
            borderColor: "black",
            borderWidth: 1,
            data: [6, 3, 4, 6]
          },
          {
            label: "NOT READ",
            backgroundColor: "white",
            borderColor: "lightbrown",
            borderWidth: 1,
            data: [2, 3, 6, 5]
          }
        ]
      };
      
      var chartOptions = {
        responsive: true,
        legend: {
          position: "top"
        },
        title: {
          display: true,
          text: "CATEGORIES"
        },
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
      
      window.onload = function() {
        var ctx = document.getElementById("canvas").getContext("2d");
        window.myBar = new Chart(ctx, {
          type: "bar",
          data: barChartData,
          options: chartOptions
        });
      };
      
      document.getElementById("textbox").innerHTML = "hi"
      console.log(window.location.href)

function getOption() {
  
  console.log(window.location.href)
  const textBox = document.getElementById("textbox")
  
  console.log(textbox.value)

  var isChecked=document.getElementById("switchValue").checked;
  console.log(isChecked);

  selectElement = document.querySelector('#choice');
  output = selectElement.value;
  console.log(output)
}

function myFunction() {
var checkBox = document.getElementById("myCheck");
var text = document.getElementById("text");
if (checkBox.checked == true){
  text.style.display = "block";
} else {
   text.style.display = "none";
}
}