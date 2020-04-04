function init() {
    makeBarPlot('weekday')
    makeBoxPlot('weekday')
}

function getData(dataset) {
    console.log("dataset changed "+dataset)
    // Changing dataset 
    makeBarPlot(dataset)
    makeBoxPlot(dataset)
}

init();