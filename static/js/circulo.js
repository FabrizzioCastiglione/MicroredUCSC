
var timeFormat = 'MM/dd/yyyy hh:mm';
const ctx = document.getElementById("Power").getContext('2d'), gradient = ctx.createLinearGradient(0, 0, 0, 450);

gradient.addColorStop(0, 'rgba(54, 162, 235, 0.7)');   
gradient.addColorStop(0.75, 'rgba(54, 162, 235, 0)');
var Potencia= new Chart(ctx, {
    type: 'line',
    data: {
        labels:  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        datasets: [{
            label: 'Potencia',
            fill: true,
            backgroundColor : gradient,
            borderColor : "#0833A2",
            borderWidth: 2,
            pointColor : "#fff",
            pointStrokeColor:"#36A2EB",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "#ff6c23",
            tension: 0.3,
            data:  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        }]
    },
    options: {}
});
   /* options: {
        scales:     {
                xAxes: [{
                    type:       "time",
                    time:       {
                        format: timeFormat,
                        tooltipFormat: 'lll'
                    },
                    scaleLabel: {
                        display:     true,
                        labelString: 'Tiempo'
                    }
                }],
                yAxes: [{
                    scaleLabel: {
                        display:     true,
                        labelString: 'Watt'
                    }
                    }]
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
    }*/
var socket = new WebSocket('ws://'+window.location.host+'/ws/graph/');
socket.onmessage = function(e){
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);

    var newGraphData = Potencia.data.datasets[0].data;
    newGraphData.shift();
    newGraphData.push(djangoData.value);
    console.log(djangoData);
    Potencia.data.datasets[0].data = newGraphData;
    Potencia.update();

}


var endpoint = '/dona/'
var donactx= document.getElementById("doughnut-chart");
var Dona = new Chart(donactx, {
    type: 'doughnut',
    data: {
          labels: ['Canal 1','Canal 2','Canal 3','Canal 4','Canal 5','Canal 6', 'Canal 7','Canal 8', 'Canal 9', 'Canal 10', 'Canal 11', 'Canal 12'],
          datasets: [{
            label: 'Potencia',
            data: [],
            backgroundColor:  ['Red', 'Orange', 'Yellow', 'Green', 'Blue','White','purple','grey','#ffce56','#36a2eb', 'rgba(75, 192, 192, 0.2)'],
            borderWidth: 1
        }]
    }
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
}, 10000);




var endpoint2 = '/FactorPotencia/'
var updatenumber = function () {
    $.ajax({
        url: endpoint2,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            let text = [];
            text =  data.FactorPotencia;
            document.getElementById("mytext").value = text;
        }
    });
}

updatenumber();
    setInterval(() => {
    updatenumber();
}, 10000);

var endpoint4 = '/Potencia_Activa/'
var updatenumber1 = function () {
    $.ajax({
        url: endpoint4,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            let text1 = [];
            text1 =  data.Potencia_Activa;
            document.getElementById("mytext1").value = text1;
        }
    });
}

updatenumber1();
    setInterval(() => {
    updatenumber1();
}, 10000);




var endpoint3 = '/PotenciaReactiva/'
var updatenumber2 = function () {
    $.ajax({
        url: endpoint3,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            let text2 = [];
            text2 =  data.PotenciaReactiva;
            document.getElementById("mytext2").value = text2;
        }
    });
}

updatenumber2();
    setInterval(() => {
    updatenumber2();
}, 10000);


 /*
            var P1 = data.P1;
            var P2 = data.P2;
            var P3 = data.P3;
            var P4 = data.P4;
            var P5 = data.P5;
            var P6 = data.P6;
            var P7 = data.P7;
            var P8 = data.P8;
            var P9 = data.P9;
            var P10 = data.P10;
            var P11 = data.P11;
            var P12 = data.P12;
            let datos = [];
            for(var i = 0; i < P1.length; i++)
            {
                datos[i] = (P1[i]+P2[i]+P3[i]+P4[i]+P5[i]+P6[i]+P7[i]+P8[i]+P9[i]+P10[i]+P11[i]+P12[i])/12;
            }*/
