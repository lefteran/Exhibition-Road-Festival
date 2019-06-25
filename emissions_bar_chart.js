// https://www.youtube.com/watch?v=sE08f4iuOhA
let emissionsBarChart = document.getElementById('emissionsBarChart').getContext('2d');

// Global Options
Chart.defaults.global.defaultFontFamily = 'Arial';
Chart.defaults.global.defaultFontSize = 14;
Chart.defaults.global.defaultFontColor = '#777';

var myData = JSON.parse(data);
var dataLength = Object.keys(myData).length;
var week1Flows = [];
var week2Flows = [];
for (i = 0; i < dataLength; i++) {
	week1Flows.push(myData[i].week1);
	week2Flows.push(myData[i].week2);
}

let massPopChart = new Chart(emissionsBarChart, {
	type:'bar', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
	data:{
		labels:['Intersection (2037150)', 'Science Museum (2033150)', 'Natural History Museum (2039150)'],
		datasets:[
			{
				label:'NO2',
				data:[week1Flows[0], week1Flows[1], week1Flows[2], week1Flows[3], week1Flows[4], week1Flows[5]],
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
				label:'PM10',
				data:[week2Flows[0], week2Flows[1], week2Flows[2], week2Flows[3], week2Flows[4], week2Flows[5]],
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
				label:'PM2.5',
				data:[week2Flows[0], week2Flows[1], week2Flows[2], week2Flows[3], week2Flows[4], week2Flows[5]],
				//backgroundColor:'green',
				backgroundColor:[
					'rgba(0, 255, 127, 0.3)',
                    'rgba(0, 255, 127, 0.3)',
                    'rgba(0, 255, 127, 0.3)'				],
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