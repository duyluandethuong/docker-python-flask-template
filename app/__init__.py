from flask import Flask

app = Flask(__name__)

# Load the webservices
from app import services