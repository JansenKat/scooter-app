Plotly.d3.json('/complaints_api', function (err, rows) {

  var classArray = unpack(rows, 'class');
  var classes = [...new Set(classArray)];

  function unpack(rows, key) {
    return rows.map(function (row) { return row[key]; });
  }

  var data = classes.map(function (classes) {
    var rowsFiltered = rows.filter(function (row) {
      return (row.class === classes);
    });
    return {
      type: 'scattermapbox',
      name: classes,
      lat: unpack(rowsFiltered, 'SR_Location_Lat'),
      lon: unpack(rowsFiltered, 'SR_Location_Lon'),
      hoverinfo: 'text',
      text: unpack(rows, 'SR_Location_Zip_Code'),
      color_discrete_sequence: ["red"],
    };
  });

  var layout = {
    title: 'Scooter Complaint Locations',
    font: {
      color: 'white'
    },
    dragmode: 'zoom',
    mapbox: {
      center: {
        lat: 30.2729,
        lon: -97.7444
      },
      domain: {
        x: [0, 1],
        y: [0, 1]
      },
      style: 'dark',
      zoom: 10
    

    },
    margin: {
      r: 20,
      t: 40,
      b: 20,
      l: 20,
      pad: 0
    },
    paper_bgcolor: '#191A1A',
    plot_bgcolor: '#191A1A',
    showlegend: false,
    annotations: [{
      x: 0,
      y: 0,
      xref: 'paper',
      yref: 'paper',
      showarrow: false
    }]
  };

  Plotly.setPlotConfig({
    mapboxAccessToken: "pk.eyJ1IjoiZXJpbmJlbnRsZXkiLCJhIjoiY2s3djN5YzNvMDcxMTNlcnl0NWljd21rMiJ9.nNWqZ59pebYdqsr6VR3qfQ"
  });

  Plotly.newPlot('complaintDiv', data, layout);
});