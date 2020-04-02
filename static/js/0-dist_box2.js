

let boxLayout = {
    title : "Trip Duration Boxplot",
    yaxis: {
        title : "Trip Duration (s)",
        showgrid : true,
        type : "log"
    }
}

function makeTraces(category) {

    let traces = []

    Plotly.d3.json('/zero_distance_api', data => {

        let map = {
            'weekday' : ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            'month_name' : ["January", "February","March","April","May","June","July","August","September","October","November","December"],
            'zip_code' : [...new Set(data.map(e => e.zip+''))].sort((a,b) => a - b),
            'hour' : [...new Set(data.map(e => e.hour+''))].sort((a,b) => a - b)
        }

        let distinct = map[category]

        distinct.forEach(function(item){
            traces.push(
                {
                    y: data.filter(element=>element[category]==item).map(element => element.trip_duration),
                    type: "box",
                    name: item,
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
            )
        })
    })
    return traces
}

function init() {
    
    let traces = makeTraces('weekday')
    console.log(traces)

    Plotly.newPlot("tester", traces, boxLayout);
}

function getData(dataset) {
    // Changing the traces 
    let traces = []
    
    switch (dataset) {
        case "zip":
            traces : makeTraces('zip')
        break;
        case "hour":
            traces : makeTraces('hour')
        break;
        case "month_name":
            traces : makeTraces('month_name')
        break;
        case "weekday":
            traces : makeTraces('weekday')
        break;
        default:
            traces : makeTraces('weekday')
        break;
    }
    console.log(traces)

    Plotly.newPlot("tester", traces, boxLayout)
}

init();