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

function EditarEvento()
{
	//AJAX
	alert("Editó el evento");
	return true;
}
function CompleteForm(myParam){
	const event = eventInformation.find(event =>event.id == myParam);
	console.log(event);
	$("#inputTitulo").val(event.title);
	$("#inputDescription").val(event.description);
	$("#inputTiempo").val(event.time);
	$("#inputImagen").val(event.imagenUrl);
}

getEventInformation();

const urlParams = new URLSearchParams(window.location.search);
const myParam = urlParams.get('id');
console.log(myParam);

CompleteForm(myParam);
