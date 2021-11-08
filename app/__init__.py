import logging
from flask import Flask

app = Flask(__name__)

from .config import Config

config = Config()
app.logger.setLevel(logging.DEBUG)

from . import routes
