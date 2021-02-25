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

function CrearEvento(evento) {

	var btnDetail = document.createElement('button');
	btnDetail.className = "btn btn-sm btn-outline-secondary";
	btnDetail.textContent = "Detalle";

	var btnComments = document.createElement('button');
	btnComments.className = "btn btn-sm btn-outline-secondary";
	btnComments.textContent = "Comentarios";

	var btnGroup = document.createElement('div');
	btnGroup.className = "btn-group";
	btnGroup.appendChild(btnDetail);
	btnGroup.appendChild(btnComments);

	var time = document.createElement('small');
	time.className = "text-muted";
	time.textContent = evento.time;

	var containerBottom = document.createElement('div');
	containerBottom.className = "d-flex justify-content-between align-items-center";
	containerBottom.appendChild(btnGroup);
	containerBottom.appendChild(time);


	var title = document.createElement('h5');
	title.className = "card-title";
	title.textContent = evento.title;

	var description = document.createElement('p');
	description.className = "card-text";
	description.textContent = evento.description;
	
	var body = document.createElement('div');
	body.className = "card-body";
	body.appendChild(title);
	body.appendChild(description);
	body.appendChild(containerBottom);

	var img = document.createElement('img');
	img.className = "card-img-top";
	img.style.cssText = "height: 250px; width: 100%; display: block;";
	img.src = evento.imagenUrl;
	img.alt = "Imagen del Evento";

	var card = document.createElement('div');
	card.className = "card mb-4 box-shadow";
	card.appendChild(img);
	card.appendChild(body);

	var col = document.createElement('div');
	col.className = "col-md-4";
	col.appendChild(card);

	return col;
}

function MostrarEventos(){
	var eventListHTML = [];

	for (let evento of eventInformation) {
		var eventHTML = CrearEvento(evento);
		eventListHTML.push(eventHTML);	
	}

	$("#Events-Container").html(eventListHTML);
}
getEventInformation();
MostrarEventos();