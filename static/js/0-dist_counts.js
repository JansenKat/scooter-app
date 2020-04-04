const day_name = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
const month_name = ["January", "February","March","April","May","June","July","August","September","October","November","December"]
 
const apiMap = {
  'weekday' : "/zero_weekday_api",
  'month_name' : "/zero_month_api",
  'hour' : "/zero_hour_api",
  'zip' : "/zero_zip_code_api"
}

let barLayout = {
  title:"Number of Trips",
  showlegend:false,
  yaxis: {
      title:"Trip Count",
      showgrid:true
    },
  plot_bgcolor:'rgba(0,0,0,0)',
  paper_bgcolor:'rgba(0,0,0,0)',
  xaxis_type : 'category'
}

//Create traces per grouping

function makeBarPlot(category) {

  Plotly.d3.json(apiMap[category], data => {

    let sortMap = {
      'weekday' : ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
      'month_name' : ["January", "February","March","April","May","June","July","August","September","October","November","December"],
      'hour' : [...new Set(data.map(e => e.hour))].sort((a,b) => a - b),
      'zip': [...new Set(data.map(e => e.zip))].sort((a,b) => a - b)
    }

    data.sort(function(a, b) {
      return sortMap[category].indexOf(a[category]) - sortMap[category].indexOf(b[category]);
    });

    let trace = [
      {
        x: data.map(element => element[category]),
        y: data.map(element => element['count(trip_duration)']),
        type: 'bar',
        marker : {
          color : 'rgb(8,81,156)'
        }
      }
    ]
    console.log(trace)

    Plotly.newPlot("nowhereBar", trace, barLayout)
  })
}
