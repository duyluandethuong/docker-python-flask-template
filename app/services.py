# Define services and routes
from flask import Flask, url_for, request, json, render_template
from app import app
import logging
import json
import os
import time

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World hahaha !!!!!!'

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500