const xlsx = require('xlsx');
const fs = require('fs');

// Leer los archivos Excel
const pricesWorkbook = xlsx.readFile('/Users/ismartinez/Sites/mdgt_finalsite/assets/db/prices.xlsx');
const productosWorkbook = xlsx.readFile('/Users/ismartinez/Sites/mdgt_finalsite/assets/db/mdgtlab_productos.xlsx');

// Convertir las hojas a JSON
const pricesData = xlsx.utils.sheet_to_json(pricesWorkbook.Sheets[pricesWorkbook.SheetNames[0]]);
const productosData = xlsx.utils.sheet_to_json(productosWorkbook.Sheets[productosWorkbook.SheetNames[0]]);

// Guardar los datos JSON en archivos
fs.writeFileSync('prices.json', JSON.stringify(pricesData, null, 2));
fs.writeFileSync('productos.json', JSON.stringify(productosData, null, 2));