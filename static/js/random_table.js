Plotly.d3.json("/random_api", function (err, rows) {

    function unpack(rows, key) {
        return rows.map(function (row) { return row[key]; });
    }

    var headerNames = Plotly.d3.keys(rows[0]);

    var headerValues = [];
    var cellValues = [];
    for (i = 0; i < headerNames.length; i++) {
        headerValue = [headerNames[i]];
        headerValues[i] = headerValue;
        cellValue = unpack(rows, headerNames[i]);
        cellValues[i] = cellValue;
    }

    var data = [{
        type: 'table',
        // columnwidth: [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],
        // columnorder: [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12],
        header: {
            values: headerValues,
            align: "center",
            line: { width: 1, color: 'rgb(50, 50, 50)' },
            fill: { color: ['007bff'] },
            font: { family: "Helvetica Neue", size: 12, color: "white" }
        },
        cells: {
            values: cellValues,
            align: ["center", "center"],
            line: { color: "black", width: 1 },
            fill: { color: ['f8f8ff'] },
            font: { family: "Helvetica Neue", size: 12, color: ["black"] }
        }
    }]

    var layout = {
        title: "Random Scooter Ride"
    }

    Plotly.newPlot('randomDiv2', data, layout);
});
