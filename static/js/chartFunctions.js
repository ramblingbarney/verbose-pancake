// create bar Chart

function createBarChart(ctx, chartlabel, labelNames, graphData, backgroundColours, borderColors){

  var myChart = new Chart(ctx, {
      type: 'horizontalBar',
      data: {
          labels: labelNames,
          datasets: [{
              label: chartlabel,
              data: graphData,
              backgroundColor: backgroundColours,
              borderColor: borderColors,
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero:true
                  }
              }]
          }
      }
  });

}
