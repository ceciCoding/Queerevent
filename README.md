# Queerevent

> All your LGBTQIA+ events in once place

---

## Table of Contents
- [Description](#description)
- [Project Structure](#project-structure)
- [Contributions](#contributions)
- [License](#license)
- [Author Info](#author-info)

--- 

## Description

Queerevent is an MVC open-sourced web application thought as a hub for LGBT+ people to post and find events within the community. The idea is to find either online, physical, one time or recurring events all over the world or in specific areas. <br>
The inspiration for this idea came to me years ago when I co-owned a vegan LGBT+ friendly restaurant in Madrid and often queer people that were visiting the city or just were new to it would ask me where to find LGTB+ workshops, parties or groups in general. The idea is that it becomes something similar to [Happy Cow](https://www.happycow.net/) but for all kinds of 'events'. It could be a podcast, a regular publication or a workshop. Everything is welcome. <br>
This is a newborn project, therefore a ton of work is yet to be done. If you want to take part in it refer to the [contributions](#contributions) section of this document.

### Technologies
- Python
- Flask
- Flask SQLAlchemy
- SQLite
- JavaScript
- jQuery
- HTML & CSS

<br>

---

## Project Structure
<br>

### The Controller

The backend of this application is managed by a Flask API divided in several modules. The [init.py](https://github.com/ceciCoding/Queerevent/blob/master/app/__init__.py) file initializes the modules. <br>
[forms.py](https://github.com/ceciCoding/Queerevent/blob/master/app/forms.py) defines and handles the validations of the forms that are used through the application using the Flask extension WTForms 2.3.3. <br>
[routes.py](https://github.com/ceciCoding/Queerevent/blob/master/app/routes.py) is the main Flask file where the view functions are defined. <br>
[helpers.py](https://github.com/ceciCoding/Queerevent/blob/master/app/helpers.py) defines some functions that are widely used through the routes file to do things such as decoding the binary files in the database with the base64 module or checking with the database if a user has a specific event added as a favorite.

All the requirements are in [requirements.txt](https://github.com/ceciCoding/Queerevent/blob/master/requirements.txt).

<br>

### The Model
The database model is defined in [models.py](https://github.com/ceciCoding/Queerevent/blob/master/app/models.py) using Flask SQLAlchemy, which allows to correlate database tables with Python classes.

<br>

### The View
The templates for this project are stored in the [app/templates](https://github.com/ceciCoding/Queerevent/tree/master/app/templates) folder as required by Flask. Within this templates directory you can also find a [macros](https://github.com/ceciCoding/Queerevent/tree/master/app/templates/macros) directory where repetitive HTML structures or components, as popups or the events container, are defined. <br>
On the other hand, the [static](https://github.com/ceciCoding/Queerevent/tree/master/app/static) directory, also required by Flask, contains assets, the CSS styles and JS files. <br>
All the CSS is written in one file (in addition to a normalize.css file to ensure cross browser compatibility). <br>
The JS, on the other hand, is divided in several files that are specific to one template or to several of them. Some of them contain some jQuery code but they are mostly written in vanilla JavaScript. The [event-details.js](https://github.com/ceciCoding/Queerevent/blob/master/app/static/event-details.js) file specifically uses the Google Maps API and the key is hidden in a file that is not under source control. If you were to use it you would need an API key of your own or feel free to write to me and I'll share mine with you. This key is also used in the controller in order to use the geocoder Python package. 

<br>

---

## Contributions

Welcome! If you are thinking about contributing first of all, thank you very much! Second, if you want to colaborate but you're not familiar with Flask and SQLAlchemy here are some resources that I've found very helpful:

- [CS50's lesson on Flask](https://www.youtube.com/watch?v=GhB6Q7KC-SM&t=1039s)
- [Another CS50's lesson on Flask](https://www.youtube.com/watch?v=EaOhKg5pKV8&t=9747s)
- [Yet another one](https://www.youtube.com/watch?v=X0dwkDh8kwA)
- [The Flask Megatutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) 
- [The Pretty Printed Youtube channel](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)
- [The Pretty Printed mini course on Flask SQLAlchemy](https://courses.prettyprinted.com/p/flask-sqlalchemy-basics)
- [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask subreddit](https://www.reddit.com/r/flask/)

If you are new to software development please don't be discouraged. I'm not a senior either. We'll figure this out together. 
Here's a list of TODOs that I have thought of. Feel free to consider other things too and send them ass pull requests.

- [ ] There are things defined in the prototype but not yet implemented in code. Here's a [link to the prortotypes](https://drive.google.com/drive/folders/1w8D80fzwlnypLSkd8e1tYqGQiTz4xbs7?usp=sharing). If you are a designer feel free to add new features.
- [ ] Send confirmation emails when a new account is created
- [ ] Improve the files upload size verification process or maybe use a library to shrink them
- [ ] Make events editable
- [ ] Bug in dates display in Safari. The scripts that handle this are event-filters.js and form-control.js
- [ ] Improve errors handling
- [ ] Make the user's photo to appear in the navbar on top
- [ ] Make it multilingual
- [ ] Implement a better searcher. At the moment it searches only event names.
- [ ] The new event description field is not paragraph sensitive. Everything displays in the event details page as one paragraph.
- [ ] If someone enters a URL for the event without the www. or https:// suffixes it won't work
- [ ] Implement the calendar connection to the database. The template and JS script are ready.
- [ ] Implement geosearch
- [ ] Implement [Google's Autocomplete for Addresses and Search Terms](https://developers.google.com/maps/documentation/javascript/places-autocomplete)
- [ ] Write the code of conduct for both this repository and Queerevent
- [ ] Write terms and conditions
- [ ] Deploy it 

<br>

---
## License 

[See it here](https://github.com/ceciCoding/Queerevent/blob/master/LICENSE)

<br>

---
## Author Info 

[Twitter](https://twitter.com/cec1_c0d) <br>
[Dev](https://dev.to/cec1_c0d) <br>
[Linkedin](https://www.linkedin.com/in/cecilia-olivera-webdev/)