//Define layout since it's consistent regardless of dataset
let boxLayout = {
    title : "Trip Duration Boxplot",
    showlegend : false,
    xaxis: {
        title : "Weekday",
        type : "category"
    },
    yaxis: {
        title : "Trip Duration (s)",
        showgrid : true,
        type : "log"
    },
    plot_bgcolor:'rgba(0,0,0,0)',
    paper_bgcolor:'rgba(0,0,0,0)'
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

        // distinct.forEach(function(item){
        for(const item of distinct) {

            let trace = {
                    y: data.filter(element=>element[category]==item).map(element => element.trip_duration),
                    type: "box",
                    name: item,
                    marker : {
                        color : 'rgb(8,81,156)',
                    },
                    line : {
                        color : 'rgb(8,81,156)'
                    }
                }
            traces.push(trace)
            Plotly.newPlot("nowhereBox", traces, boxLayout)
        }
    })
}