function buildTable(sample) {

    let s = d3.json(`/zipcode/${sample}`).then((data) => {

        //Make Table
        var tableData = [{
            type: 'table',
            header: {
                values: headerValues,
                align: "center",
                line: { width: 1, color: 'rgb(50, 50, 50)' },
                fill: { color: ['rgb(0,191,255)'] },
                font: { family: "Helvetica Neue", size: 12, color: "white" }
            },
            cells: {
                values: cellValues,
                align: ["center", "center"],
                line: { color: "black", width: 1 },
                fill: { color: ['rgb(240,248,255)'] },
                font: { family: "Helvetica Neue", size: 12, color: ["black"] }
            }
        }]

        Plotly.newPlot("zipcodeDiv", tableData)

    })
}

function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");

    // Use the list of sample names to populate the select options
    d3.json("/zipcode_api").then((sampleNames) => {
        sampleNames.forEach((sample) => {
            selector
                .append("option")
                .text(sample)
                .property("value", sample);
        });

        // Use the first sample from the list to build the initial plots
        const firstSample = sampleNames[0];
        buildTable(firstSample);
    });
}

function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    console.log(`option changed: ${newSample} selected`)
    buildTable(newSample);
}

// Initialize the dashboard
init();