Plotly.d3.json('/duration_api', function(err, rows){
  console.log(rows)
    function unpack(rows, key) {
        return rows.map(function(row) { return row[key]; });}

    function getMaxOfArray(numArray) {
        return Math.max.apply(null, numArray);
    }
    var scl =['rgb(213,62,79)','rgb(244,109,67)','rgb(253,174,97)','rgb(254,224,139)','rgb(255,255,191)','rgb(230,245,152)','rgb(171,221,164)','rgb(102,194,165)','rgb(50,136,189)','rgb(60,176,129)'];
    var data = [];
    var count = unpack(rows, 'trip_distance');
    console.log(count)
    console.log(rows)
    var startLongitude = unpack(rows, 'start_lon');
    var endLongitude = unpack(rows, 'end_lon')
    var startLat = unpack(rows, 'start_lat');
    var endLat = unpack(rows, 'end_lat');
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
                width: 2,
                color: scl[i]
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
      style: "dark",
      // // layers: [
      //   {
      //     sourcetype: "raster",
      //     source: ["https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"],
      //     below: "traces"
      //   }
      // ],
      center: { lat: 30.2280314, lon: -97.7734004 },
      zoom: 10
    },
    margin: { r: 0, t: 0, b: 0, l: 0 }
  };

  Plotly.setPlotConfig({
    mapboxAccessToken:"pk.eyJ1Ijoic2toYW4wNyIsImEiOiJjazg4dXNsNmUwMGFuM2ZudHNiaXU1Y3kwIn0.uDCrOvOHUNL7qdsiOUwMPA"
  });

  Plotly.newPlot('myDiv1', data, layout, {displayModeBar: false})

  ;

});


