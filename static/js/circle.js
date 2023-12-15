var endpoint = '/dona/'
var ctx = document.getElementById("doughnut-chart");
var Dona = new Chart(ctx, {
    type: 'doughnut',
    data: {
          labels: ['Canal 1','Canal 2','Canal 3','Canal 4','Canal 5','Canal 6', 'Canal 7','Canal 8', 'Canal 9', 'Canal 10', 'Canal 11', 'Canal 12'],
          datasets: [{
            label: 'Potencia',
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