// function buildCharts() {

Plotly.d3.json('/redzone_api', function(data) {
            console.log(data)
    let zip = []
    let complaint = []
    for ( var i = 0 ; i < data.length; i++ ) { 
      zip.push(`zip ${data[i].zip_code}`);
      complaint.push(data[i].complaint_count);
    console.log(zip)
    console.log(complaint)
    



      let bar_data = {
        textsrc:{type:"string"}, 
        type:"bar",
        x: zip,
        y: complaint,
        mode: 'markers',
        // marker: {
        //           color: , 
        //           size: sample_values.map(d => d)
        //         },
        hovertext: complaint

      }
    
      let bar_layout = {
        title: "Worst Zipcode to Leave a Scooter In"
        
      }
    
      Plotly.newPlot("red-zoneDiv2", [bar_data], bar_layout);
    }
})

// var xValue = ['Product A', 'Product B', 'Product C'];

// var yValue = [20, 14, 23];
// var trace1 = {
//     x: xValue,
//     y: yValue,
//     type: 'bar',
//     text: yValue.map(String),
//     textposition: 'auto',
//     hoverinfo: 'none',
//     marker: {
//       color: 'rgb(158,202,225)',
//       opacity: 0.6,
//       line: {
//         color: 'rgb(8,48,107)',
//         width: 1.5
//       }
//     }
//   };
  
//   var data = [trace1];
  
//   var layout = {
//     title: 'January 2013 Sales Report',
//     barmode: 'stack'
//   };
  
//   Plotly.newPlot('red-zoneDiv2', data, layout);
