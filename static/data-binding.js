//taken from this tutorial: https://bit.ly/34vC9AT for binding data in JS
class Binding {
    constructor(prop, handler, el) {
        this.prop = prop;
        this.handler = handler;
        this.el = el;
    }
    bind() {
        let bindingHandler = Binder.handlers[this.handler];
        bindingHandler.bind(this);
        Binder.subscribe(this.prop, () => {
            bindingHandler.react(this);
        });
    }
    setValue(value) {
        Binder.scope[this.prop] = value;
    }
    getValue() {
        return Binder.scope[this.prop];
    }
}


class Binder {
    static setScope(scope) {
        this.scope = scope;
    }
    static redefine() {
        let keys = Object.keys(this.scope);
        keys.forEach((key) => {
            let value = this.scope[key];
            delete this.scope[key];
            Object.defineProperty(this.scope, key, {
                get() {
                    return value;
                },
                set(newValue) {
                    const shouldNotify = value != newValue;
                    value = newValue;
                    if (shouldNotify) {
                        Binder.notify(key);
                    };
                }
            })
        });
    }
    static subscribe(key, callback) {
        this.subscriptions.push({
            key: key,
            cb: callback
        });
    }
    static notify(key) {
        const subscriptions = this.subscriptions.filter(
            subscription => subscription.key == key
        );
        subscriptions.forEach(subscription => {
            subscription.cb();
        })
    }
}

class ValueBindingHandler {
    bind(binding) {
        binding.el.addEventListener('input', () => {
            this.listener(binding);
        });
        this.react(binding);
    }
    react(binding) {
        binding.el.value = binding.getValue();
    }
    listener(binding) {
        let value = binding.el.value;
        binding.setValue(value);
    }
}


class TextBindingHandler {
    bind(binding) {
        this.react(binding);
    }
    react(binding) {
        binding.el.innerText = binding.getValue();
    }
}

// create some static properties
Binder.subscriptions = [];
Binder.scope = {};
Binder.handlers = {
    value: new ValueBindingHandler(),
    text: new TextBindingHandler()
}

const dateString = new Date().toString();

Binder.setScope({
    name: 'Event Name',
    place: 'Somewhere',
    periodicity: 'Every Monday',
    date: dateString.slice(0, 16),
    startingHour: '4:00 PM',
    endingHour: '8:00 PM',
    organizer: 'Organizer',
    website: 'https://example.com',
    link: 'Link',
    description: 'Awesome event taking place somewhere today organized by amazing people. Wear your finest outfit.'
});
Binder.redefine();

const els = document.querySelectorAll('[data-bind]');
els.forEach(el => {
    const expressionParts = el.getAttribute('data-bind').split(':');
    const bindingHandler = expressionParts[0].trim();
    const scopeKey = expressionParts[1].trim();
    const binding = new Binding(scopeKey, bindingHandler, el);
    binding.bind();
});


//img upload preview (taken from stackoverflow)
function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#prv-img').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("#img-upload").change(function() {
  readURL(this);
});

//const declarations and event listeners
const typeOfEvent = document.querySelector('.select-type');
const locationInput = document.querySelector('.location');
const placePreview = document.querySelector('.place');
const datePreview = document.querySelector('.date');
const dateInput = document.querySelector('#date-input');
const periodicityOption = document.querySelector('.select-period');
const periodicityInput = document.querySelector('.period');
const periodicityPreview = document.querySelector('.periodicity');

//handling showing or not the location input
typeOfEvent.addEventListener('change', () => {
    typeOfEvent.style.color = 'black';
    if (typeOfEvent.value === 'Online') {
        locationInput.style.display = 'none';
        placePreview.style.display = 'none';
    } else {
        locationInput.style.display = 'flex';
        placePreview.style.display = 'block';
    }   
})

//handle showing or not periodicity
periodicityOption.addEventListener('change', () => {
    periodicityOption.style.color = 'black';
    if (periodicityOption.value === 'Recurring') {
        periodicityInput.style.display = 'flex';
        periodicityPreview.style.display = 'block';
        datePreview.style.display = 'none';
        dateInput.style.display = 'none';
    } else {
        periodicityInput.style.display = 'none';
        periodicityPreview.style.display = 'none';
        datePreview.style.display = 'block';
        dateInput.style.display = 'flex';
    }
})

//preview date correctly
dateInput.addEventListener('change', () => {
    const newDate = new Date(dateInput.querySelector('input').value);
    const newDateStr = newDate.toString();
    datePreview.innerHTML = newDateStr.slice(0, 16);
})

//change font color for inputs when active (placeholder can't be passed with binding logic)
document.querySelector('.form').addEventListener('click', (e) => {
    if (e.target.type === 'text') {
          e.preventDefault();
     }
    if (e.target.className === 'inpt') {
        e.target.style.color = 'black';       
    }
})
