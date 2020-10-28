'use strict';

//dynamic height
const mapContainer = document.querySelector('.map');
mapContainer.style.height = `${mapContainer.offsetWidth * 0.7}px`;

// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyCb8eFJlYyBxSkuRVETVvzWEJqyy4kGeBI&callback=initMap';
script.defer = true;

const iconBase = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/';
// Attach your callback function to the `window` object
window.initMap = function() {
  // JS API is loaded and available
    const map = new google.maps.Map(mapContainer, {
        center: { lat: 37.946051, lng: -1.131742 },
        zoom: 15
    });

    const marker = new google.maps.Marker({
        position: { lat: 37.946051, lng: -1.131742 },
        map: map
    })
};

// Append the 'script' element to 'head'
document.head.appendChild(script);

