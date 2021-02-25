from os import environ
import API

app = API.app 
wsgi_app = app.wsgi_app
