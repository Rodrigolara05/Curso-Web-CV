// Mi archivo JS
// Variables (Tipo nombre_variable;) var, let, const
var nombre = 'Rodrigo';
var primer_apellido = "Lara";
var segundo_apellido = "Camarena";
var edad = 35;
var es_mayor_de_edad = true; 
var materiales = ["Mouse","Laptop","Colonia","Monitor"];

// Variables, definicion, concatenacion, reasignacion, Arrays

var nombre_completo = nombre + " " + primer_apellido;
console.log("Nombre completo: " + nombre_completo); 

nombre_completo = nombre + " " + primer_apellido + " " + segundo_apellido;
console.log("Nombre completo: " + nombre_completo); 

console.log("Edad: " + edad);
console.log("Es mayor de edad: " + es_mayor_de_edad);

console.log(materiales);
materiales.push("Billetera");
console.log(materiales);

var notas = [18,15,13,20];
notas.sort();
console.log(notas);

//var oracion = `Mi nombre es ${nombre} y mi apellido es ${primer_apellido}`; // PLUS

//Condicionales
es_mayor_de_edad = !es_mayor_de_edad; // Simbolo "!"" revierte el valor de un boolean

if(es_mayor_de_edad){
	console.log("El usuario es mayor de edad");
}
else{
	console.log("El usuario NO es mayor de edad");	
}

//Funciones

//No return a value (void)
function example(){
	let edad = 28; 
	console.log(edad);
}
function example2(){
	let edad = 53; 
	console.log(edad);
}

//Return a value (Int)
function multiplica(){
	const a = 10;
	const b = 5;
	const result = a * b;
	return result;
}
console.log(multiplica());

// Ciclos
//----While----//
/*
while(true){
	//console.log("este es un ciclo");
}
*/
//----For----//
//For tradicional
for(let i=0; i<materiales.length; i++){
	console.log(materiales[i]);
}
//Muestra los indices
for(var number in materiales){
	if(number>2){
		continue; // Saltar codigo que sigue y continuar el incremento de numero en for
	}
	console.log(number);
}

//Muestra los datos
for(var item of materiales){
	console.log(item);	
}