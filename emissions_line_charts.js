let emissionsLineChart33 = document.getElementById('emissionsLineChart33').getContext('2d');
let emissionsLineChart37 = document.getElementById('emissionsLineChart37').getContext('2d');
let emissionsLineChart39 = document.getElementById('emissionsLineChart39').getContext('2d');

var myData = JSON.parse(data);

var no2_33_emissions = [];
var pm10_33_emissions = [];
var pm25_33_emissions = [];

var no2_37_emissions = [];
var pm10_37_emissions = [];
var pm25_37_emissions = [];

var no2_39_emissions = [];
var pm10_39_emissions = [];
var pm25_39_emissions = [];


var i;
for(i=3; i<=11; i++){
    no2_33_value = (myData[i].no2_33 == 0) ? null : myData[i].no2_33;
    no2_33_emissions.push(no2_33_value);
    pm10_33_value = (myData[i].pm10_33 == 0) ? null : myData[i].pm10_33;
    pm10_33_emissions.push(pm10_33_value);
    pm25_33_value = (myData[i].pm25_33 == 0) ? null : myData[i].pm25_33;
    pm25_33_emissions.push(pm25_33_value);

    no2_37_value = (myData[i].no2_37 == 0) ? null : myData[i].no2_37;
    no2_37_emissions.push(no2_37_value);
    pm10_37_value = (myData[i].pm10_37 == 0) ? null : myData[i].pm10_37;
    pm10_37_emissions.push(pm10_37_value);
    pm25_37_value = (myData[i].pm25_37 == 0) ? null : myData[i].pm25_37;
    pm25_37_emissions.push(pm25_37_value);

    no2_39_value = (myData[i].no2_39 == 0) ? null : myData[i].no2_39;
    no2_39_emissions.push(no2_39_value);
    pm10_39_value = (myData[i].pm10_39 == 0) ? null : myData[i].pm10_39;
    pm10_39_emissions.push(pm10_39_value);
    pm25_39_value = (myData[i].pm25_39 == 0) ? null : myData[i].pm25_39;
    pm25_39_emissions.push(pm25_39_value);
}


let theEmissionsLineChart33 = new Chart(emissionsLineChart33, {
    type: 'line',
    data: {
        labels: ["Saturday 22/6", "Sunday 23/6", "Monday 24/6", "Tuesday 25/6", "Wednesday 26/6", "Thursday 27/6", "Friday 28/6", "Saturday 29/6", "Sunday 30/6"],
        datasets: [
            {
                label: "NO\u2082",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(255, 99, 132, 1)",
                borderColor: "rgba(255, 99, 132, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(255, 99, 132, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 4,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(255, 99, 132, 1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 5,
                pointRadius: 1,
                pointHitRadius: 1,
                data: [no2_33_emissions[0], no2_33_emissions[1], no2_33_emissions[2], no2_33_emissions[3], no2_33_emissions[4], no2_33_emissions[5], no2_33_emissions[6], no2_33_emissions[7], no2_33_emissions[8]]
            },
            {
                label: "PM\u2081\u2080",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(50, 150, 250, 1)",
                borderColor: "rgba(50, 150, 250, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(50, 150, 250, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 4,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(50, 150, 250, 1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 5,
                pointRadius: 1,
                pointHitRadius: 1,
                data: [pm10_33_emissions[0], pm10_33_emissions[1], pm10_33_emissions[2], pm10_33_emissions[3], pm10_33_emissions[4], pm10_33_emissions[5], pm10_33_emissions[6]]
            },
            {
                label: "PM\u2082.\u2085",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(0, 255, 127, 1)",
                borderColor: "rgba(0, 255, 127, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(0, 255, 127, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 4,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(0, 255, 127, 1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 5,
                pointRadius: 1,
                pointHitRadius: 1,
                data: [pm25_33_emissions[0], pm25_33_emissions[1], pm25_33_emissions[2], pm25_33_emissions[3], pm25_33_emissions[4], pm25_33_emissions[5], pm25_33_emissions[6]]
            },
        ]
    }

});


let theEmissionsLineChart37 = new Chart(emissionsLineChart37, {
    type: 'line',
    data: {
        labels: ["Saturday 22/6", "Sunday 23/6", "Monday 24/6", "Tuesday 25/6", "Wednesday 26/6", "Thursday 27/6", "Friday 28/6", "Saturday 29/6", "Sunday 30/6"],
        datasets: [
            {
                label: "NO\u2082",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(255, 99, 132, 1)",
                borderColor: "rgba(255, 99, 132, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(255, 99, 132, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 4,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(255, 99, 132, 1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 5,
                pointRadius: 1,
                pointHitRadius: 1,
                data: [no2_37_emissions[0], no2_37_emissions[1], no2_37_emissions[2], no2_37_emissions[3], no2_37_emissions[4], no2_37_emissions[5], no2_37_emissions[6], no2_37_emissions[7], no2_37_emissions[8]]
            },
            {
                label: "PM\u2081\u2080",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(50, 150, 250, 1)",
                borderColor: "rgba(50, 150, 250, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(50, 150, 250, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 4,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(50, 150, 250, 1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 5,
                pointRadius: 1,
                pointHitRadius: 1,
                data: [pm10_37_emissions[0], pm10_37_emissions[1], pm10_37_emissions[2], pm10_37_emissions[3], pm10_37_emissions[4], pm10_37_emissions[5], pm10_37_emissions[6]]
            },
            {
                label: "PM\u2082.\u2085",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(0, 255, 127, 1)",
                borderColor: "rgba(0, 255, 127, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(0, 255, 127, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 4,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(0, 255, 127, 1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 5,
                pointRadius: 1,
                pointHitRadius: 1,
                data: [pm25_37_emissions[0], pm25_37_emissions[1], pm25_37_emissions[2], pm25_37_emissions[3], pm25_37_emissions[4], pm25_37_emissions[5], pm25_37_emissions[6]]
            },
        ]
    }

});


let theEmissionsLineChart39 = new Chart(emissionsLineChart39, {
    type: 'line',
    data: {
        labels: ["Saturday 22/6", "Sunday 23/6", "Monday 24/6", "Tuesday 25/6", "Wednesday 26/6", "Thursday 27/6", "Friday 28/6", "Saturday 29/6", "Sunday 30/6"],
        datasets: [
            {
                label: "NO\u2082",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(255, 99, 132, 1)",
                borderColor: "rgba(255, 99, 132, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(255, 99, 132, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 4,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(255, 99, 132, 1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 5,
                pointRadius: 1,
                pointHitRadius: 1,
                data: [no2_39_emissions[0], no2_39_emissions[1], no2_39_emissions[2], no2_39_emissions[3], no2_39_emissions[4], no2_39_emissions[5], no2_39_emissions[6], no2_39_emissions[7], no2_39_emissions[8]]
            },
            {
                label: "PM\u2081\u2080",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(50, 150, 250, 1)",
                borderColor: "rgba(50, 150, 250, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(50, 150, 250, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 4,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(50, 150, 250, 1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 5,
                pointRadius: 1,
                pointHitRadius: 1,
                data: [pm10_39_emissions[0], pm10_39_emissions[1], pm10_39_emissions[2], pm10_39_emissions[3], pm10_39_emissions[4], pm10_39_emissions[5], pm10_39_emissions[6]]
            },
            {
                label: "PM\u2082.\u2085",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(0, 255, 127, 1)",
                borderColor: "rgba(0, 255, 127, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(0, 255, 127, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 4,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(0, 255, 127, 1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 5,
                pointRadius: 1,
                pointHitRadius: 1,
                data: [pm25_39_emissions[0], pm25_39_emissions[1], pm25_39_emissions[2], pm25_39_emissions[3], pm25_39_emissions[4], pm25_39_emissions[5], pm25_39_emissions[6]]
            },
        ]
    }

});