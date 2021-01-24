//Example con ID
/*
var boton = $("#btn-aparecer");
console.log(boton);
//boton.removeClass("btn-primary");
console.log(boton);
//boton.addClass("btn-success");
console.log(boton);

boton.click(function(){
	var parrafo = $("#texto");
	parrafo.removeClass("hide");
});

$("#btn-desaparecer").click(function(){
	var parrafo = $("#texto");
	parrafo.addClass("hide");
});

boton.addEventListener("click", function(){
	console.log("click");
});
*/
var coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
	coll[i].addEventListener("click", function(){
		this.classList.toggle("active");
		var content = this.nextElementSibling;
		if(content.style.maxHeight){
			content.style.maxHeight = null;
		}else{
			content.style.maxHeight = content.scrollHeight + "px";
		}
	});	
}


$("#btn-add").click(function(){
	var key = $("#input-key").val();
	if(key==="")
	{
		console.log("El campo key esta vacio");
		//err-input-value
		$("#err-input-key").text("El campo clave esta vacio");
		return false;
	}

	var value = $("#input-value").val();
	if(value==="")
		{
		console.log("El campo value esta vacio");
		$("#err-input-value").text("El campo key esta vacio");
		return false;
		}
	localStorage.setItem(key,value);
	$("#input-key").val("");
	$("#input-value").val("");
});

$("#btn-search").click(function(){
	var key = $("#input-key").val();
	if(key==="")
	{
		console.log("El campo key esta vacio");
		return false;
	}
	const value = localStorage.getItem(key);
	if(value != null)
	{console.log(value);$("#input-key").val("");
	$("#input-value").val("");}
	else{
		console.log("La clave no existe");
	}
});

$("#btn-remove").click(function(){
	var key = $("#input-key").val();
	if(key==="")
	{
		console.log("El campo key esta vacio");
		return false;
	}
	localStorage.removeItem(key);
	$("#input-key").val("");
	$("#input-value").val("");
});