const fs = require('fs');
const path = './purged';

// Crear el directorio de salida si no existe
if (!fs.existsSync(path)){
  fs.mkdirSync(path);
}

module.exports = {
  content: ['./**/*.html', './assets/**/*.js'], // Archivos donde PurgeCSS buscará las clases CSS utilizadas
  css: [
    './assets/css/animate.min.css',
    './assets/css/bootstrap.min.css',
    './assets/css/custom-font.css',
    './assets/css/font-awesome.min.css',
    './assets/css/fontawesome-pro.css',
    './assets/css/magnific-popup.css',
    './assets/css/main.css',
    './assets/css/slick.css',
    './assets/css/spacing.css',
    './assets/css/style.css',
    './assets/css/swiper.min.css'
  ],
  output: './purged/', // Directorio donde se guardarán los archivos purgados
};
