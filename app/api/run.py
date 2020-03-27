#!/usr/bin/env python3

import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from api import encoder

from api.config import DATABASE_CONNECTION_URI

print(DATABASE_CONNECTION_URI)

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'krisenheld:in-API'}, pythonic_params=True)

application = app.app # expose global WSGI application object

# Get the underlying Flask app instance
flask_app = application

# Configure the SQLAlchemy part of the app instance
flask_app.config['SQLALCHEMY_ECHO'] = True
flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(flask_app)

# Initialize Marshmallow
ma = Marshmallow(flask_app)

print("testing DB connection..")
db.session.execute("SELECT 1")