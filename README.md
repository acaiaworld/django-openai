# Django Development with OpenAI API: A Step-by-Step Guide

![Django Development with OpenAI API](/django-openai.png?raw=true "Django Development with OpenAI API")

This is a code repository for a Django web development project that integrates the OpenAI API. It provides a step-by-step guide on how to use the OpenAI API in a Django application to build intelligent chatbots and other interactive features.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have the following software installed on your machine:

- Python 3
- Django
- openai

You will also need to sign up for an OpenAI API key at https://beta.openai.com/.


### Installing

To set up the Django project on your local machine, follow these steps:

1. Clone the repository:

```sh
$ git clone https://github.com/acaiaworld/django-openai.git
$ cd django-openai
```

2. Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

3. Install the required Python packages:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.


4. Set up your OpenAI API key in the openai.api_key.set() function in mychatbot/views.py.



5. Run the Django development server:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
6. Navigate to http://127.0.0.1:8000/ in your web browser to view the chatbot interface.



## Built With
* [Django](https://www.djangoproject.com/) - The web framework used
* [OpenAI API](https://beta.openai.com/) - Advanced machine learning models


## Author

ACAIA 2023 - [@ACAIA](https://www.facebook.com/acaiaworld) - info@acaiaworld.com

ACAIA Website: [https://www.acaiaworld.com/](https://www.acaiaworld.com/)