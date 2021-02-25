function CrearEvento(){
	var result = false;

	var titulo = $("#inputTitulo").val().toString();
	var descripcion = $("#inputDescripcion").val().toString();
	var tiempo = $("#inputTiempo").val().toString();
	var imagenUrl = $("#inputImagen").val().toString();
	
	tiempo += " horas";

	var user = localStorage.getItem('user');
	var objUser = JSON.parse(user);

	json = {
		id:0,
		titulo: titulo,
		descripcion : descripcion,
		tiempo : tiempo,
		imagenUrl: imagenUrl,
		usuarioId: objUser.id
	};

	data = JSON.stringify(json);

	$.ajax({
		url: "https://eventsoftv2.azurewebsites.net/evento/save",
		type: "POST",
		contentType: "application/json",
		dataType: 'json',
		data: data,
		async: false,
		success: function(respuesta){
			result = (respuesta.data.toString() == 'true')
			alert(respuesta.mensaje);
		},
		error: function(e){
			console.log(e);
		}
	});

	return result;
}