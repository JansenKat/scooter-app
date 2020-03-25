Plotly.d3.csv('final_copy.csv', function(err, rows){
    function unpack(rows, key) {
        return rows.map(function(row) { return row[key]; });}

    function getMaxOfArray(numArray) {
        return Math.max.apply(null, numArray);
    }

    var data = [];
    var count = unpack(rows, 'cnt');
    console.log(count)
    console.log(rows)
    var startLongitude = unpack(rows, 'startLon');
    var endLongitude = unpack(rows, 'endLon')
    var startLat = unpack(rows, 'startLat');
    var endLat = unpack(rows, 'endLat');
    console.log("ending cordinates" + endLat);
    console.log("starting cordinates" + startLat);
    console.log("start long" + startLongitude);
  
    console.log("end long" + endLongitude);
    for ( var i = 0 ; i < count.length; i++ ) {
        var opacityValue = count[i]/getMaxOfArray(count);

        var result = {
            type: 'scattermapbox',
            locationmode: 'USA-states',
            projection: 'albers usa',
            lon: [ endLongitude[i] , startLongitude[i]],
            lat: [ startLat[i] , endLat[i]],
            mode: 'lines+markers',
            line: {
                width: 10,
                color: 'red'
            },
            opacity: opacityValue
        }
        data.push(result);
    };

  // var layout = {
  //     title: 'Longest Ride',
  //     showlegend: true,
  //     geo:{
  //         scope: 'texas',
  //             lataxis: {
  //       range: [ 25, 35 ],
  //     },
  //     lonaxis:{
  //       range: [-100, -90],
  //     },
  //         showsubunits: true,
  //         showland: true,
  //         showlakes: true,
  //       showrivers: true
  //     }
      
  // };

  var layout = {
    dragmode: "zoom",
    mapbox: {
      style: "white-bg",
      layers: [
        {
          sourcetype: "raster",
          source: ["https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"],
          below: "traces"
        }
      ],
      center: { lat: 30.2280314, lon: -97.7734004 },
      zoom: 10
    },
    margin: { r: 0, t: 0, b: 0, l: 0 }
  };

    Plotly.newPlot("myDiv", data, layout, {showLink: false});

});


