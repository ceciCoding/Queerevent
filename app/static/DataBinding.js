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

