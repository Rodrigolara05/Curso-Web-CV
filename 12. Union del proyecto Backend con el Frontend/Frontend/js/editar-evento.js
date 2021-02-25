var eventInformation = [];

const urlParams = new URLSearchParams(window.location.search);
const myParam = urlParams.get('id');

function EditarEvento()
{
	var result = false;
	var id = myParam;
	var titulo = $("#inputTitulo").val().toString();
	var descripcion = $("#inputDescripcion").val().toString();
	var tiempo = $("#inputTiempo").val().toString();
	var imagenUrl = $("#inputImagen").val().toString();


	var user = localStorage.getItem('user');
	var objUser = JSON.parse(user);

	json ={
		id: id,
		titulo:titulo,
		descripcion:descripcion,
		tiempo:tiempo,
		imagenUrl,imagenUrl,
		usuarioId:objUser.id
	};

	data = JSON.stringify(json);

	$.ajax({
		url: "http://localhost:7070/evento/update",
		type: "PUT",
		contentType : 'application/json',
		dataType: 'json',
		data: data,
		async: false,
		success: function(respuesta){
			console.log(respuesta);
			result = (respuesta.data.toString() == 'true');
			alert(respuesta.mensaje);
		},
		error: function(e){
			console.log(e);
		}
	});

	return result;
}

function CompleteForm(myParam){
	let objEvent = null

	$.ajax({
		url : "http://localhost:7070/evento/" + myParam,
		type: "GET",
		success: function(respuesta){
			for(var item of respuesta.data){
				obj = JSON.parse(item);
				console.log(obj)
				objEvent = new Evento(obj.id,obj.imagenUrl,obj.titulo,obj.descripcion,obj.tiempo);
			}
			$("#inputTitulo").val(objEvent.titulo);
			$("#inputDescripcion").val(objEvent.descripcion);
			$("#inputTiempo").val(objEvent.tiempo);
			$("#inputImagen").val(objEvent.imagenUrl);
		},
		error: function(e){
			console.log(e);
		}
	});
}

CompleteForm(myParam);
