function titleCase(str) { 
    return str.toLowerCase().split('_').map(function(word) { 
      return (word.charAt(0).toUpperCase() + word.slice(1)); 
    }).join(' '); 
  } 

function init() {
    makeBarPlot('weekday')
    makeBoxPlot('weekday')
}

function getData(dataset) {

    barLayout.xaxis.title = titleCase(dataset)
    boxLayout.xaxis.title = titleCase(dataset)

    //clear existing plots
    Plotly.newPlot("nowhereBar", [], barLayout)
    Plotly.newPlot("nowhereBox", [], boxLayout)

    // Changing dataset 
    makeBarPlot(dataset)
    makeBoxPlot(dataset)
}

init();