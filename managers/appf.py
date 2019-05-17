import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sys

app = Flask(__name__)



db = SQLAlchemy(app)
ma = Marshmallow(app)

sys.path.insert(0, 'views')

if __name__ == '__main__':
    app.run(debug=True)
