from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

# Initialize app and database connection
app = Flask(__name__)
CORS(app, resources={"/api/*": {"origins": "*"}}, supports_credentials=True)

# Konfigurasi MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://gamingdb2_gravityyes:3dca44b250bc6e23465e85dffae6a52dcea09ecd@ho9nc.h.filess.io:3305/gamingdb2_gravityyes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'test123'
db = SQLAlchemy(app)

app.app_context().push()
