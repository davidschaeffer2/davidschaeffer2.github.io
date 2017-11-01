# app/__init__.py
# David Schaeffer
# 10/23/2017


from flask import Flask


app = Flask(__name__)
app.config.from_object('config')
