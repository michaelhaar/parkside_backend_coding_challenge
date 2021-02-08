# Parkside Robo-Dance Coding Challenge (Backend) 🤖

## Introduction

This repository was part of my job application process at [Parkside](https://www.parkside-interactive.com/) and contains a simple REST API that shows my current skills and talent as well as my preferred work style. I was asked to built the backend for a **Robo-Dance** competition app.

## Overview

Robots love dancing and regularly battle each other in fabulous dance competitions. Goal of the project was to design a API for a Robo-Dance competition app in a way that a frontend application could consume it. Therefore I created two API endpoints with the following features:

- **/robots**

  - add a robot
  - receive a individual robot
  - receive all robots
  - (data is stored in a persisted data source)

- **/danceoffs**
  - store a danceoff result
  - store multiple danceoff results with a single request
  - receive all danceoffs
  - receive a specific danceoff

Please checkout the [original project description from Parkside](docs/Parkside_Coding_Challenge_Backend.pdf) for more information.

## My Solution

## Outlook

### What I would do better if I have more time?

- discuss project requirements in more detail
- add authorization and protect _create_ endpoints
- add further validation for the danceoff _bulk_create_ endpoint and add more unit tests
- provide a leaderboard feature

### How would I set up the frontend app?

First, I would try to define the requirements, which would probably give me something like this:

- the user should be able to start a new competition.
  - 10 distinct robots will be picked randomly
  - robots will be split into two teams
- the user should be able to start the competition.
  - each robot battles one robot from the opponent team
  - randomly choose a winner
  - send results to the backend using the API

Next, I would plan the architecture and the frameworks for the frontend. It would probably look like this:

- inside the django project, create a new django app called `frontend`
  - setup everything (urls, templates, static files, etc. )
- use [React](https://reactjs.org/) (maybe also [Redux](https://redux.js.org/), [React Router](https://reactrouter.com/) and [Bootstrap](https://getbootstrap.com/)) to build the frontend application
  - use [Axios](https://github.com/axios/axios) to make API calls
  - use [webpack](https://webpack.js.org/) to compile the Javascript code
- use Github `issues`, Git-Flow and feature branches to track the progress and organize my tasks
- some UI/UX mockups might be helpful
  - create the first drafts by hand and then use [Figma](https://www.figma.com/) for more details

## Used Frameworks, Libraries and APIs

- **[Django](https://www.djangoproject.com/)**: web framework for perfectionists with deadlines.
- **[Django REST Framework](https://www.django-rest-framework.org/)**: powerful and flexible toolkit for building Web APIs.
- **[drf-yasg](https://github.com/axnsan12/drf-yasg)**: generate OpenAPI 2.0 documentation
- for production/hosting:
  - **[gunicorn](https://gunicorn.org/)**: Python WSGI HTTP Server for UNIX
  - **[psycopg2](https://www.psycopg.org)**: most popular PostgreSQL adapter for the Python
  - **[django-environ](https://django-environ.readthedocs.io/en/latest/)**: utilize 12factor inspired environment variables
  - **[whitenoise](http://whitenoise.evans.io/en/stable/)**: simplifies static file serving for Python web apps
  - **[Heroku](https://www.heroku.com/)**: platform as a service

## Author

👤 **Michael Haar**

- LinkedIn: [@michaelhaar](https://www.linkedin.com/in/michaelhaar/)
- Github: [@michaelhaar](https://github.com/michaelhaar)
- Email: michael.haar@gmx.at
