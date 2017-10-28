# app/__init__.py
# David Schaeffer
# 10/23/2017


from flask import Flask
from flask_frozen import Freezer


app = Flask(__name__)
app.config.from_pyfile('config.py')
freezer = Freezer(app)
