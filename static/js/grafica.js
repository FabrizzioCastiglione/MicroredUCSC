var endpoint = /Potencia/
var timeFormat = 'MM/dd/yyyy hh:mm';
const ctx = document.getElementById('Power').getContext('2d');
var gradient = ctx.createLinearGradient(0, 0, 0, 600);
gradient.addColorStop(0, 'rgba(54, 162, 235, 0.7)');   
gradient.addColorStop(0.75, 'rgba(54, 162, 235, 0)');

const Potencia= new Chart(ctx, {
    type: 'line',
    data: {
        labels:  [],
        datasets: [{
            label: '# of Votes',
            fill: true,
            backgroundColor : gradient,
            borderColor : "#0833A2",
            borderWidth: 2,
            pointColor : "#fff",
            pointStrokeColor:"#36A2EB",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "#ff6c23",
            tension: 0.3,
            data: []
        }]
    },
    options: {
      scales: {
            xAxes: [{
                type: 'time',
                time: {
                   format: timeFormat
                }
            }]
        }, 
        responsive: true,
        datasetStrokeWidth : 3,
        pointDotStrokeWidth : 4
    },
    plugins: {
      zoom: {
          pan: {
              enabled: true,
              mode: 'xy',
          },
          zoom: {
              enabled: true,
              mode: 'x'
          }
      }
    }
});

var updateChart = function () {
    $.ajax({
        url: endpoint,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
             function newDate(variable) {
                let exit = [];
                for (let i = 0; i < variable.length; i++) {
                    auxdatos = new Date(variable[i]);
                    exit.push(auxdatos)
                }
                return exit;
            }
            //Grafica voltaje
            Potencia.data.labels = newDate(data.tiempo);
            Potencia.data.datasets[0].data = data.Potencia;
            
            //Update
            Potencia.update();
        }
    });
}

updateChart();
setInterval(() => {
    updateChart();
}, 60000);


var endpoint = '/dona/'
var donactx = document.getElementById("doughnut-chart");
var pieCtx = document.getElementById("doughnut-chart");
var Dona = new donct(donactx, {
    type: 'doughnut',
    data: {
          labels: ['Canal 1','Canal 2','Canal 3','Canal 4','Canal 5','Canal 6', 'Canal 7','Canal 8', 'Canal 9', 'Canal 10', 'Canal 11', 'Canal 12'],
          datasets: [{
            label: '# of Votes',
            data: [],
            backgroundColor:  ['Red', 'Orange', 'Yellow', 'Green', 'Blue','White','purple','grey','#ffce56','#36a2eb', 'rgba(75, 192, 192, 0.2)'],
            borderWidth: 1
        }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Chart.js Doughnut Chart'
        }
      }
    },
  });
      
var updateChart = function () {
  $.ajax({
      url: endpoint,
      type: 'GET',
      dataType: 'json',
      success: function (data) {
          //Grafica voltaje
          Dona.data.datasets[0].data =  [data.P1,data.P2,data.P3,data.P4,data.P5,data.P6,data.P7,data.P8,data.P9,data.P10,data.P11,data.P12];
          //Update
          Dona.update();
      }
  });
}
updateChart();
setInterval(() => {
    updateChart();
}, 60000);




var endpoint2 = /FactorPotencia/
var test = [endpoint2];
document.getElementById("mytext").value = test;
console.log(test);

var updatenumber = function () {
    $.ajax({
        url: endpoint2,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            //Grafica voltaje
            test =  data.FactorPotencia;
            //Update
            test.update();
        }
    });
}

updatenumber();
    setInterval(() => {
    updatenumber();
}, 10000);
