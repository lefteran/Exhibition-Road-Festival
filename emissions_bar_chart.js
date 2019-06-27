// https://www.youtube.com/watch?v=sE08f4iuOhA
let emissionsBarChart = document.getElementById('emissionsBarChart').getContext('2d');

// Global Options
Chart.defaults.global.defaultFontFamily = 'Arial';
Chart.defaults.global.defaultFontSize = 14;
Chart.defaults.global.defaultFontColor = '#777';

var myData = JSON.parse(data);
var dataLength = Object.keys(myData).length;

var sensor1Emissions = [];
var sensor2Emissions = [];
var sensor3Emissions = [];

sensor1Emissions.push(myData[0].no2_1516);
sensor1Emissions.push(myData[0].no2Old);
sensor1Emissions.push(myData[0].no2New);
sensor1Emissions.push(myData[0].pm10_1516);
sensor1Emissions.push(myData[0].pm10Old);
sensor1Emissions.push(myData[0].pm10New);
sensor1Emissions.push(myData[0].pm25_1516);
sensor1Emissions.push(myData[0].pm25Old);
sensor1Emissions.push(myData[0].pm25New);

sensor2Emissions.push(myData[1].no2_1516);
sensor2Emissions.push(myData[1].no2Old);
sensor2Emissions.push(myData[1].no2New);
sensor2Emissions.push(myData[1].pm10_1516);
sensor2Emissions.push(myData[1].pm10Old);
sensor2Emissions.push(myData[1].pm10New);
sensor2Emissions.push(myData[1].pm25_1516);
sensor2Emissions.push(myData[1].pm25Old);
sensor2Emissions.push(myData[1].pm25New);


sensor3Emissions.push(myData[2].no2_1516);
sensor3Emissions.push(myData[2].no2Old);
sensor3Emissions.push(myData[2].no2New);
sensor3Emissions.push(myData[2].pm10_1516);
sensor3Emissions.push(myData[2].pm10Old);
sensor3Emissions.push(myData[2].pm10New);
sensor3Emissions.push(myData[2].pm25_1516);
sensor3Emissions.push(myData[2].pm25Old);
sensor3Emissions.push(myData[2].pm25New);


let massPopChart = new Chart(emissionsBarChart, {
	type:'bar', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
	data:{
		labels:['Intersection (2037150)', 'Science Museum (2033150)', 'Natural History Museum (2039150)'],
		datasets:[
			{
				label:'NO2 - 15,16/06/2019',
				data:[sensor1Emissions[0], sensor2Emissions[0], sensor3Emissions[0]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(255, 99, 132, 0.6)',
					'rgba(255, 99, 132, 0.6)',
					'rgba(255, 99, 132, 0.6)'
				],
				borderWidth:1,
				borderColor:'#777',
				hoverBorderWidth:3,
				hoverBorderColor:'#000'
			},
			{
				label:'NO2 - 22,23/06/2019',
				data:[sensor1Emissions[1], sensor2Emissions[1], sensor3Emissions[1]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(255, 99, 132, 0.8)',
					'rgba(255, 99, 132, 0.8)',
					'rgba(255, 99, 132, 0.8)'
				],
				borderWidth:1,
				borderColor:'#777',
				hoverBorderWidth:3,
				hoverBorderColor:'#000'
			},
			{
				label:'NO2 - 29/06/2019',
				data:[sensor1Emissions[2], sensor2Emissions[2], sensor3Emissions[2]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(255, 99, 132, 1)',
					'rgba(255, 99, 132, 1)',
					'rgba(255, 99, 132, 1)'
				],
				borderWidth:1,
				borderColor:'#777',
				hoverBorderWidth:3,
				hoverBorderColor:'#000'
			},
			{
				label:'PM10 - 15,16/06/2019',
				data:[sensor1Emissions[3], sensor2Emissions[3], sensor3Emissions[3]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(50, 150, 250, 0.3)',
					'rgba(50, 150, 250, 0.3)',
					'rgba(50, 150, 250, 0.3)'
				],
				borderWidth:1,
				borderColor:'#777',
				hoverBorderWidth:3,
				hoverBorderColor:'#000'
			},
			{
				label:'PM10 - 22,23/06/2019',
				data:[sensor1Emissions[4], sensor2Emissions[4], sensor3Emissions[4]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(50, 150, 250, 0.6)',
					'rgba(50, 150, 250, 0.6)',
					'rgba(50, 150, 250, 0.6)'
				],
				borderWidth:1,
				borderColor:'#777',
				hoverBorderWidth:3,
				hoverBorderColor:'#000'
			},
			{
				label:'PM10 - 29/06/2019',
				data:[sensor1Emissions[5], sensor2Emissions[5], sensor3Emissions[5]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(50, 150, 250, 0.8)',
					'rgba(50, 150, 250, 0.8)',
					'rgba(50, 150, 250, 0.8)'
				],
				borderWidth:1,
				borderColor:'#777',
				hoverBorderWidth:3,
				hoverBorderColor:'#000'
			},
			{
				label:'PM2.5 - 15,16/06/2019',
				data:[sensor1Emissions[6], sensor2Emissions[6], sensor3Emissions[6]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(0, 255, 127, 0.3)',
                    'rgba(0, 255, 127, 0.3)',
                    'rgba(0, 255, 127, 0.3)'				],
				borderWidth:1,
				borderColor:'#777',
				hoverBorderWidth:3,
				hoverBorderColor:'#000'
			},
            {
				label:'PM2.5 - 22,23/06/2019',
				data:[sensor1Emissions[7], sensor2Emissions[7], sensor3Emissions[7]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(0, 255, 127, 0.6)',
                    'rgba(0, 255, 127, 0.6)',
                    'rgba(0, 255, 127, 0.6)'				],
				borderWidth:1,
				borderColor:'#777',
				hoverBorderWidth:3,
				hoverBorderColor:'#000'
			},
			{
				label:'PM2.5 - 29/06/2019',
				data:[sensor1Emissions[8], sensor2Emissions[8], sensor3Emissions[8]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(0, 255, 127, 0.8)',
                    'rgba(0, 255, 127, 0.8)',
                    'rgba(0, 255, 127, 0.8)'				],
				borderWidth:1,
				borderColor:'#777',
				hoverBorderWidth:3,
				hoverBorderColor:'#000'
			}
		]
	},
	options:{
		title:{
			display:true,
			text:'Average emissions',
			fontSize:25
		},
		legend:{
			display:true,
			position:'right',
			labels:{
				fontColor:'#000'
			}
		},
		layout:{
			padding:{
				left:50,
				right:0,
				bottom:0,
				top:0
			}
		},
		tooltips:{
			enabled:true
		}
	}
});