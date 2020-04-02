Plotly.d3.json('/zero_distance_api', data => {

// create trace per weekday
let sunday = {
  y: data.filter(element=>element.weekday=="Sunday").map(element => element.trip_duration),
  type: "box",
  name: "Sunday",
  boxpoints : 'suspectedoutliers',
  marker : {
      color : 'rgb(8,81,156)',
      outliercolor : 'rgba(219, 64, 82, 0.6)',
      line : {
          outliercolor : 'rgba(219, 64, 82, 0.6)',
          outlierwidth : 2
      }
  },
  line : {
      color : 'rgb(8,81,156)'
  }
}

let monday = {
    y : data.filter(element=>element.weekday=="Monday").map(element => element.trip_duration),
    type : "box",
    name : "Monday",
    boxpoints : 'suspectedoutliers',
    marker : {
        color : 'rgb(8,81,156)',
        outliercolor : 'rgba(219, 64, 82, 0.6)',
        line : {
            outliercolor : 'rgba(219, 64, 82, 0.6)',
            outlierwidth : 2
        }
    },
    line : {
        color : 'rgb(8,81,156)'
    }
}
let tuesday = {
  y: data.filter(element=>element.weekday=="Tuesday").map(element => element.trip_duration),
  type: "box",
  name: "Tuesday",
  boxpoints : 'suspectedoutliers',
  marker : {
      color : 'rgb(8,81,156)',
      outliercolor : 'rgba(219, 64, 82, 0.6)',
      line : {
          outliercolor : 'rgba(219, 64, 82, 0.6)',
          outlierwidth : 2
      }
  },
  line : {
      color : 'rgb(8,81,156)'
  }
}
let wednesday = {
  y: data.filter(element=>element.weekday=="Wednesday").map(element => element.trip_duration),
  type: "box",
  name: "Wednesday",
  boxpoints : 'suspectedoutliers',
  marker : {
      color : 'rgb(8,81,156)',
      outliercolor : 'rgba(219, 64, 82, 0.6)',
      line : {
          outliercolor : 'rgba(219, 64, 82, 0.6)',
          outlierwidth : 2
      }
  },
  line : {
      color : 'rgb(8,81,156)'
  }
}
let thursday = {
  y: data.filter(element=>element.weekday=="Thursday").map(element => element.trip_duration),
  type: "box",
  name: "Thursday",
  boxpoints : 'suspectedoutliers',
  marker : {
      color : 'rgb(8,81,156)',
      outliercolor : 'rgba(219, 64, 82, 0.6)',
      line : {
          outliercolor : 'rgba(219, 64, 82, 0.6)',
          outlierwidth : 2
      }
  },
  line : {
      color : 'rgb(8,81,156)'
  }
}
let friday = {
  y: data.filter(element=>element.weekday=="Friday").map(element => element.trip_duration),
  type: "box",
  name: "Friday",
  boxpoints : 'suspectedoutliers',
  marker : {
      color : 'rgb(8,81,156)',
      outliercolor : 'rgba(219, 64, 82, 0.6)',
      line : {
          outliercolor : 'rgba(219, 64, 82, 0.6)',
          outlierwidth : 2
      }
  },
  line : {
      color : 'rgb(8,81,156)'
  }
}
let saturday = {
  y: data.filter(element=>element.weekday=="Saturday").map(element => element.trip_duration),
  type: "box",
  name: "Saturday",
  boxpoints : 'suspectedoutliers',
  marker : {
      color : 'rgb(8,81,156)',
      outliercolor : 'rgba(219, 64, 82, 0.6)',
      line : {
          outliercolor : 'rgba(219, 64, 82, 0.6)',
          outlierwidth : 2
      }
  },
  line : {
      color : 'rgb(8,81,156)'
  }
}

let boxData = [sunday, monday, tuesday, wednesday, thursday, friday, saturday] 

//Set up layout
let boxLayout = {
        title : "Trip Duration Boxplot by Weekday",
        yaxis: {
            title : "Trip Duration (s)",
            showgrid : true,
            type : "log"
        }

    }

Plotly.plot("tester", boxData, boxLayout)

})