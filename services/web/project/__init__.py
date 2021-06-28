from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
#register_blueprints(app)
db = SQLAlchemy()

from project import routes
