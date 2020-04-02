const day_name = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
const month_name = ["January", "February","March","April","May","June","July","August","September","October","November","December"]
 

//Create traces per grouping
let zip_trace = [
  {
    x: zipcode.index,
    y: zipcodes['trip_id'],
    type: 'bar'
  }
];

let week_trace = [
  {
    x: day_name,
    y: weekdays['trip_id'],
    type: 'bar'
  }
];

let hour_trace = [
  {
    x: hours.index,
    y: hours['trip_id'],
    type: 'bar'
  }
];

let month_trace = [
  {
    x: month_name,
    y: months['trip_id'],
    type: 'bar'
  }
];

count_data = [zip_trace, week_trace, hour_trace, month_trace]

//Add menu to flip between groupings
let updatemenus=[
  {
      buttons: [
          {
            label = "Zipcode",
            method = "update",
            args = [{"visible": [True, False, False, False]}]
          },
          {
            label = "Weekday",
            method = "update",
            args = [{"visible": [True, False, False, False]}]
          },
          {
            label = "Hours",
            method = "update",
            args = [{"visible": [True, False, False, False]}]
          },
          {
            label = "Months",
            method = "update",
            args = [{"visible": [True, False, False, False]}]
          },
      ],
      active : 0
      showactive: true,
      type: 'buttons',
      x : 1.00,
      y : 1.10,
      yanchor : 'top',
  }
]

let count_layout = {
    title:"Number of Trips",
    showlegend:False,
    autosize:False,
    width:1000,
    height:800,
    yaxis: {
        title:"Trip Count",
        showgrid:True
      },
    updatemenus:updatemenus,
    plot_bgcolor:'rgba(0,0,0,0)',
    paper_bgcolor:'rgba(0,0,0,0)',
    xaxis_type : 'category'
}

Plotly.newPlot("myDiv", count_data, count_layout)