//Define layout since it's consistent regardless of dataset
let boxLayout = {
    title : "Trip Duration Boxplot",
    showlegend : false,
    yaxis: {
        title : "Trip Duration (s)",
        showgrid : true,
        type : "log"
    },
    xaxis_type : 'category'
}


//Function to define and gather the traces for whichever category
function makeBoxPlot(category) {

    let traces = []

    Plotly.d3.json('/zero_distance_api', data => {

        console.log(category + " box data retrieved")
        
        //This will define the distinct options and order them correctly
        //Chronological ordering for weekday, month_name and hour, 
        let map = {
            'weekday' : ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            'month_name' : ["January", "February","March","April","May","June","July","August","September","October","November","December"],
            'hour' : [...new Set(data.map(e => e.hour))].sort((a,b) => a - b),
            'zip': [...new Set(data.map(e => e.zip))].slice(0,20)
        }

        let distinct = map[category]

        console.log(distinct)

        Plotly.newPlot("nowhereBox", traces, boxLayout)

        distinct.forEach(function(item){

            let trace = {
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
            Plotly.addTraces("nowhereBox", trace)
        })
    })
    return traces
}