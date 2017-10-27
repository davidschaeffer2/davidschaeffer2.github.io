# app/__init__.py
# David Schaeffer
# 10/23/2017


from flask import Flask
from flask_frozen import Freezer


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
freezer = Freezer(app)
