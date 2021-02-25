function Registrarse(){
	var result = false;

	var correo = $("#inputEmail").val().toString();
	var nombres = $("#inputNombres").val().toString();
	var apellidos = $("#inputApellidos").val().toString();
	var contrasenia = $("#inputPassword").val().toString();

	json = {
		id: 0,
		correo : correo,
		nombres : nombres,
		apellidos : apellidos,
		contrasenia : contrasenia
	};

	data = JSON.stringify(json);


	$.ajax(
	{
		url: "http://localhost:7070/usuario/save",
		type: "POST",
		contentType : "application/json",
		dataType : 'json',
		data : data,
		async: false,
		success:function(respuesta){
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