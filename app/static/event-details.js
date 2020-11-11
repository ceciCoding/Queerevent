//TODO: Dynamic height not working with the maps API
'use strict';
const key = config.googleAPIKey

// Create the script tag, set the appropriate attributes
const script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=' + key + '&callback=initMap';
script.defer = true;

//dynamic height
const mapContainer = document.querySelector('.map') || null;
if (mapContainer) {
    mapContainer.style.height = `${mapContainer.offsetWidth * 0.7}px`;
} 

// Attach your callback function to the `window` object
window.initMap = function () {
    const address = document.querySelector('.location');
    const coordinates = {
        lat: Number(address.getAttribute(['data-lat'])),
        lng: Number(address.getAttribute(['data-lng']))
    }
  // JS API is loaded and available
    const map = new google.maps.Map(mapContainer, {
        center: {
            lat: coordinates.lat,
            lng: coordinates.lng
        },
        zoom: 10
    });

    const marker = new google.maps.Marker({
        position: {
            lat: coordinates.lat,
            lng: coordinates.lng
        },
        map: map
    })
};

// Append the 'script' element to 'head'
document.head.appendChild(script);