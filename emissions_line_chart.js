let emissionsLineChart = document.getElementById('emissionsLineChart').getContext('2d');

let theEmissionsLineChart = new Chart(emissionsLineChart, {
    type: 'line',
    data: {
        labels: ["Saturday 22/6", "Sunday 23/6", "Monday 24/6", "Tuesday 25/6", "Wednesday 26/6", "Thursday 27/6", "Friday 28/6", "Saturday 29/6", "Sunday 30/6"],
        datasets: [
            {
                label: "NO2",
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
                data: [65, 59, 80, 81, 16, 55, 40]
            },
            {
                label: "PM10",
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
                data: [28, 48, 40, 19, 86, 27, 90]
            },
            {
                label: "PM2.5",
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
                data: [10, 85, 60, 54, 70, 42, 55]
            },
        ]
    }

});