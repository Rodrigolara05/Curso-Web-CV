//max.rodrigo@gmail.com
//12345678910
function IniciarSesion(){
	var result = false;

	var correo = $("#inputEmail").val().toString()
	var contrasenia = $("#inputPassword").val().toString()

	json = {
		correo : correo,
		contrasenia : contrasenia
	};

	data = JSON.stringify(json);

	$.ajax(
	{
		url: "http://localhost:7070/usuario/login",
		type: "POST",
		contentType: "application/json",
		dataType: "json",
		data: data,
		async: false,
		success: function(respuesta){
			var msg = respuesta.mensaje;
			obj = JSON.parse(respuesta.data);
			localStorage.setItem('user',JSON.stringify(obj))
			alert(msg);
			result = true;
		},
		error: function(e){
			alert("Servicio no disponible");
			console.log(e);
		}
	});

	return result;
} 