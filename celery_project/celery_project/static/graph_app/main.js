const ctx = document.getElementById('myChart').getContext('2d');

var graphData = {
        type: 'line',
        data: {
          labels: ['January', 'February', 'March', 'April', 'May', 'June'],
          datasets: [{
            label: 'Demo graph',
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1,
          }]
        },
        options: {}
}


var myChart = new Chart(ctx, graphData);


var socket = new WebSocket("ws://" + window.location.host + "/ws/graph/");

socket.onmessage = function(e) {
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);

    var newGraphData = graphData.data.datasets[0].data;

    newGraphData.shift();
    newGraphData.push(djangoData.value);

    graphData.data.datasets[0].data = newGraphData;
    myChart.update();
}