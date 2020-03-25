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
    var startLongitude = unpack(rows, 'startlon');
    var endLongitude = startLongitude;
    var startLat = unpack(rows, 'starting cordinates');
    var endLat = unpack(rows, 'endlat');
    console.log("end lat" + endLat);
    console.log("starting cordinates" + startLat);
    console.log("start long" + startLongitude);
  
    console.log("end long" + endLongitude);
    for ( var i = 0 ; i < count.length; i++ ) {
        var opacityValue = count[i]/getMaxOfArray(count);

        var result = {
            type: 'scattergeo',
            locationmode: 'https://data.austintexas.gov/api/views/cb9m-wucg/rows.json?accessType=DOWNLOAD',
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

  var layout = {
      title: 'Longest Ride',
      showlegend: true,
      geo:{
          scope: 'austin, texas',
              lataxis: {
        range: [ 25, 35 ],
      },
      lonaxis:{
        range: [-100, -90],
      },
          showsubunits: true,
          showland: true,
          showlakes: true,
        showrivers: true
      }
  };


    Plotly.newPlot("myDiv", data, layout, {showLink: false});

});


