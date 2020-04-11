
Plotly.d3.json('/redzone_api', function(data) {
    let zip = []
    let complaint = []
    for ( var i = 0 ; i < data.length; i++ ) { 
      zip.push(`zip ${data[i].zip_code}`);
      complaint.push(data[i].complaint_count);
    

  


      let bar_data = {
        textsrc:{type:"string"}, 
        type:"bar",
        x: zip,
        y: complaint.sort(function(a, b){return b-a}),
        mode: 'markers',

    
        hovertext: complaint

      }
    
      let bar_layout = {
        title: "Worst Zipcode to Leave a Scooter In"
        
      }
    
      Plotly.newPlot("red-zoneDiv2", [bar_data], bar_layout);
    }
})


