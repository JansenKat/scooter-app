function init() {
    makeBarPlot('weekday')
    makeBoxPlot('weekday')
}

function getData(dataset) {

    console.log("dataset changed "+dataset)

    //clear existing plots
    Plotly.newPlot("nowhereBar", [], barLayout)
    Plotly.newPlot("nowhereBox", [], boxLayout)

    // Changing dataset 
    makeBarPlot(dataset)
    makeBoxPlot(dataset)
}

init();