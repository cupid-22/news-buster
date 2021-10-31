from flask import Flask
from .helper.configuration import configure_app

app = Flask(__name__, template_folder='templates')
configure_app(app)

from . import routes
