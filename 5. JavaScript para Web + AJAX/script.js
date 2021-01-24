var lista_de_paises = [];

class Pais{
	constructor(name,region,sub_region,capital){
		this.name = name;
		this.region = region;
		this.subregion = sub_region;
		this.capital = capital;			
	}
}

function ObtenerPaises(codigo){
	$.ajax({
		url: 'https://restcountries.eu/rest/v2/regionalbloc/' + codigo,
		success: function(respuesta){
			for(var pais of respuesta){
				let objPais = new Pais(pais.name,pais.region,pais.subregion,pais.capital);
				lista_de_paises.push(objPais);
				ActualizarTabla(lista_de_paises);
			}
		},
		error: function(){

		}
	});
}

function ActualizarTabla(paises){
	var table = document.createElement('table');
	var body = document.createElement('tbody');
	var row = document.createElement('tr');	
	
	var cell = document.createElement('th');
	var text = document.createTextNode("Capital");
	cell.appendChild(text);
	row.appendChild(cell);

	cell = document.createElement('th');
	text = document.createTextNode("Nombre del Pais");
	cell.appendChild(text);
	row.appendChild(cell);

	cell = document.createElement('th');
	text = document.createTextNode("Region");
	cell.appendChild(text);
	row.appendChild(cell);

	cell = document.createElement('th');
	text = document.createTextNode("Sub-Region");
	cell.appendChild(text);
	row.appendChild(cell);
	body.appendChild(row);

	for(let pais of paises){
		row = document.createElement('tr');
		
		cell = document.createElement('td');
		text = document.createTextNode(pais.capital);
		cell.appendChild(text);
		row.appendChild(cell);

		cell = document.createElement('td');
		text = document.createTextNode(pais.name);
		cell.appendChild(text);
		row.appendChild(cell);

		cell = document.createElement('td');
		text = document.createTextNode(pais.region);
		cell.appendChild(text);
		row.appendChild(cell);

		cell = document.createElement('td');
		text = document.createTextNode(pais.subregion);
		cell.appendChild(text);
		row.appendChild(cell);

		body.appendChild(row);
	}
	table.appendChild(body);
	$("#tableContent").html(table);
}

function IsValidData(id,texto,error){
	if(texto == ""){
		$(id).text(error);
		return false;
	}
	else{
		$(id).text("");
		return true;
	}
}

function AgregarPais(){
	$("#btn-subir").click(function(){

	var input_nombre = $("#input-nombre");
	var nombre = input_nombre.val();
	if(!IsValidData("#error-nombre", nombre, "Nombre no puede ser vacio"))
		return;
	
	var input_region = $("#input-region");
	var region = input_region.val();
	if(!IsValidData("#error-region", region, "Region no puede ser vacio"))
		return;

	var input_sub_region = $("#input-sub-region");
	var sub_region = input_sub_region.val();
	if(!IsValidData("#error-sub-region", sub_region, "Sub-Region no puede ser vacio"))
		return;

	var input_capital = $("#input-capital");
	var capital = input_capital.val();
	if(!IsValidData("#error-capital", capital, "Capital no puede ser vacio"))
		return;

	let pais = new Pais(nombre,region,sub_region,capital);
	lista_de_paises.push(pais);
	ActualizarTabla(lista_de_paises);
	});
}

function ImportarPaises(){
	$("#btn-importar").click(function(){
		var region = $("#cb-regiones").val();
		ObtenerPaises(region);
	});
}
function LimpiarTabla(){
	$("#btn-limpiar").click(function(){
		lista_de_paises = [];
		ActualizarTabla(lista_de_paises);
	});
}
AgregarPais();
ImportarPaises();
LimpiarTabla();