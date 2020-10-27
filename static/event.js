'use strict';

//dynamic height
const map = document.querySelector('.map');
map.style.height = `${map.offsetWidth * 0.6}px`;

// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyCb8eFJlYyBxSkuRVETVvzWEJqyy4kGeBI&callback=initMap';
script.defer = true;

// Attach your callback function to the `window` object
window.initMap = function() {
  // JS API is loaded and available
    new google.maps.Map(map, {
        center: {lat: -34.397, lng: 150.644},
        zoom: 12

    })
};

// Append the 'script' element to 'head'
document.head.appendChild(script);

