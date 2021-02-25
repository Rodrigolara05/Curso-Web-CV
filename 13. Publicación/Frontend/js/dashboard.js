var eventInformation = [];

function getEventsAPI(){
	var user = localStorage.getItem('user');
	var objUser = JSON.parse(user);
	$.ajax(
	{
		url:"https://eventsoftv2.azurewebsites.net/evento/usuario/" + objUser.id,
		type: "GET",
		success: function(respuesta){
			for (var item of respuesta.data) {
				obj = JSON.parse(item);
				let objEvent = new Evento(obj.id,obj.imagenUrl, obj.titulo, obj.descripcion, obj.tiempo);
				eventInformation.push(objEvent);
			}
			MostrarEventos(eventInformation);		
		},
		error: function(e){
			console.log(e);
		}
	});

}

function AñadirEvento(evento){
	var row = document.createElement('tr');
	var cell = document.createElement('td');
	cell.textContent = evento.id;
	row.appendChild(cell);
	
	cell = document.createElement('td');
	cell.textContent = evento.titulo;
	row.appendChild(cell);

	cell = document.createElement('td');
	cell.textContent = evento.tiempo;
	row.appendChild(cell);

	var editar = document.createElement('a');
	editar.textContent = "Editar";
	editar.href = "editar-evento.html?id=" + evento.id;

	var eliminar = document.createElement('a');
	eliminar.textContent = "Eliminar";
	eliminar.href = "#"; 	

	eliminar.addEventListener("click", function(e){
		var result = false;
		$.ajax(
		{
			url: "http://localhost:7070/evento/delete/" + evento.id,
			type: "DELETE",
			async: false,
			success: function(respuesta){
				console.log(respuesta);	
				result = (respuesta.data.toString()=='true');	
			},
			error: function(e){
				console.log(e);
			}
		});
		if(result){
			location.reload();
		}
		else{
			alert("No se eliminó el registro");
		}
	});	

	var space = document.createElement('span');
	space.textContent = "    ";

	cell = document.createElement('td');
	cell.appendChild(editar);
	cell.appendChild(space);
	cell.appendChild(eliminar);

	row.appendChild(cell);
	return row;
}

function MostrarEventos(data){
	var eventListHTML = [];
	for(let evento of data){
		var row = AñadirEvento(evento);
		eventListHTML.push(row);
	}
	$("#tableBody").html(eventListHTML);
}

getEventsAPI();