var eventInformation = [];

function getEventInformation(){
	//AJAX
	let objEvent = new Evento(
		1,
		"https://image.freepik.com/vector-gratis/plantilla-cartel-evento-musical-formas-abstractas_1361-1316.jpg",
		"Musica Elecronica",
		"Disfruta la mejor musica electronica en los domos de San Miguel junto con los mejores representantes del género",
		"2 horas");
	let objEvent2 = new Evento(
		2,
		"https://image.freepik.com/vector-gratis/plantilla-poster-evento-musical-formas-coloridas_1361-1591.jpg",
		"Musica Elecronica en San Isidro",
		"Disfruta la mejor musica electronica en los domos de San Isidro junto con los mejores representantes del género",
		"4 horas");
	let objEvent3 = new Evento(
		3,
		"https://image.freepik.com/vector-gratis/plantilla-poster-evento-musica-moderna_1361-1292.jpg",
		"Musica moderna",
		"Disfruta la mejor musica moderna en el estadio nacional junto con los mejores representantes del género",
		"6 horas");

	let objEvent4 = new Evento(
		4,
		"https://image.freepik.com/vector-gratis/plantilla-cartel-evento-formas-abstractas_1361-1291.jpg",
		"Musica criolla",
		"Disfruta la mejor musica criolla en el estadio matute junto con los mejores representantes del género",
		"5 horas");

	eventInformation.push(objEvent);	
	eventInformation.push(objEvent2);	
	eventInformation.push(objEvent3);	
	eventInformation.push(objEvent4);	
}


function AñadirEvento(evento){
	var row = document.createElement('tr');
	var cell = document.createElement('td');
	cell.textContent = evento.id;
	row.appendChild(cell);
	
	cell = document.createElement('td');
	cell.textContent = evento.title;
	row.appendChild(cell);

	cell = document.createElement('td');
	cell.textContent = evento.time;
	row.appendChild(cell);

	var editar = document.createElement('a');
	editar.textContent = "Editar";
	editar.href = "editar-evento.html?id=" + evento.id;

	var eliminar = document.createElement('a');
	eliminar.textContent = "Eliminar";
	eliminar.href = "#"; 	

	var space = document.createElement('span');
	space.textContent = "    ";

	cell = document.createElement('td');
	cell.appendChild(editar);
	cell.appendChild(space);
	cell.appendChild(eliminar);

	row.appendChild(cell);
	return row;
}

function MostrarEventos(){
	var eventListHTML = [];
	for(let evento of eventInformation){
		var row = AñadirEvento(evento);
		eventListHTML.push(row);
	}
	$("#tableBody").html(eventListHTML);
}
getEventInformation();
MostrarEventos();