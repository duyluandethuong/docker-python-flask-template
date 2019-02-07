# [START app]
import logging
import os
from flask import Flask
from flask_cors import CORS
from app import app
CORS(app)

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    debug_status_env = os.environ['DEBUG']
    if debug_status_env.lower() == 'true':
        is_debug_enabled = True
    else:
        is_debug_enabled = False

    app.run(host='0.0.0.0', port=5000, debug=is_debug_enabled)
# [END app]
