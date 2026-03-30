// Inicializar el mapa centrado en Buenos Aires
let map = L.map('map').setView([-34.6037, -58.3816], 13);

// Cargar capa base (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Añadir un marcador
let marker = L.marker([-34.6037, -58.3816]).addTo(map);

// Popup al hacer clic en el marcador
marker.bindPopup("<b>Buenos Aires</b><br>Capital de Argentina").openPopup();

// agrea un circulo
let circle = L.circle([ -34.6037, -58.3816], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);

// agrega un poligono
let polygon = L.polygon([
    [ -34.6037, -58.3820],
    [ -34.6097, -58.3836],
    [ -34.6057, -58.3866]
]).addTo(map);

// popup al hacer clic para ver las coordenadas
let popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent(e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);