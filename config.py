from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

# Initialize app and database connection
app = Flask(__name__)
CORS(app, resources={"/api/*": {"origins": "*"}}, supports_credentials=True)

# Konfigurasi MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://mcw_01:mcw123@localhost:3306/web2_db'
# mysql+mysqlconnector://apigames_itstypehim:29b0b9e4dc840a16808d694ac2a2203e813bc7b7@z0f3t.h.filess.io:3305/apigames_itstypehim
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'test123'
db = SQLAlchemy(app)

app.app_context().push()