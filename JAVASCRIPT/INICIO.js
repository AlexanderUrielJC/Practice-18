//PARA HACER COMENTARIOS SOLO BASTA CON PONER LOS (//)
// Y NO SE TOMARA EN CUENTA PARA EL CODIGO
///En JS se utilizan valores como es el caso de: Undefined, null, boolean, string, symbol, number y object.
var miVariable = 'freeCodeCamp';

console.log(miVariable);

miVariable=16;
console.log(miVariable);

var a; // variable undefined
var b = 18; // con valor definido
// sin olvidar que siempre para comprobar hay que poner 
//Console.log seguido de la variable

//Ejemplo

var a; 
var b = 18;

console.log(a)
console.log(b)

var a = b

var x = 10; // inicializar la variable

var miIdioma = 'Español';

//Es importante llevar a cabo las variables tal cual como le hemos asignado su nombre
// de lo contrario saldria Error variable is not difined

//Sumas: operacion artmeticas

var suma = 7 + 12;

console.log(suma);

var resta = 150 - 20; // positivo
console.log(resta);

resta = 20-150; // negativo

resta = 150 -150;// resultado es 0
console.log(resta);

///Multiplicacion

var producto = 5 * 3;
console.long(producto)

producto = 9 * 0;
console.log(producto);

// division 

var cociente = 20/2
console.log(cociente);

cociente =17 / 31;
console.log(cociente);

cociente = 2/0;
console.log(cociente); // Como resultado es infinity

//Numeros decimales
var miNumeroDecimal = 18.8;
//Ejemplo
var peso = 18.88;
// MUltiplicar numeros decimales

var producto = 73.4 * 18.7;
console.log(producto);

producto = 4.5 * 5
console.log(producto);

producto= -5.7 * -19.38;

//Dividir nume decimales

var cociente = 5.0/10.0;// Independientemente de que el numero sea .0, en JS se piensa que se esta trabajando con decimales.

// Resto de una division

var resto = 15 % 5;
console.log(resta);

resto = 5 % 1;
console.log(resta);

// incrementar el valor de una Variable
var librosComprados = 105;
console.log(librosComprados); //inicialmente

//Opcion 1

librosComprados = librosComprados + 1;
console.log(librosComprados);

//Opcion 2

librosComprados++; // se agraga uno en la variable colocando dos signos
console.log(librosComprados);

//Reducir el valor de una variable

var numeroDeEstudiantes = 256;
console.log(numeroDeEstudiantes);

numeroDeEstudiantes = numeroDeEstudiantes - 1;
console.log(numeroDeEstudiantes); // se resta en valor 1 a la variable asignada

numeroDeEstudiantes --; // igual que en el caso de suma, se resta en valor de 1 al colocar doble (--)
console.log(numeroDeEstudiantes);

// asignacion  de Suma
var a = 23;

a = a + 5;
console.log(a);

// Opcion 2 
var a = 23;
a += 5;


var totalVentas = 13567.34
console.log(totalVentas);

totalVentas += 345.67
console.log(totalVentas);

//Reducir valor de una variable

var b = 18;
b -= 56,
console.log(b);

//ejemplo

var totalDeDeudas= 2446;

totalDeDeudas  -= 345;
console.log(totalDeDeudas); // teniendo como resultado final 2101 como deuda total

// asignacion de multiplicacion
var c = 23;

c = c * 2;
console.log(c);

c *= 2;
console.log(c);

var Salario = 45000;
console.log(Salario);
aumento = 550
resultado=Salario + aumento;
console.log(resultado);

//Dvision

var d = 39;
d /= 3;

console.log(d);

var Salario = 1500;
console.log(Salario);

Salario/=3
console.log(Salario);


////CADENAS DE CARACTRES
var Nombre = 'Alan';
var Apellido = 'Hernandez';
Nombre= Nombre + Apellido
console.log(Nombre);

var Materia = 'Macroeconomia';
console.log(Materia);

console.log(materia)