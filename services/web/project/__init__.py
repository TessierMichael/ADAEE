from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy()
db.init_app(app)

from project import routes
