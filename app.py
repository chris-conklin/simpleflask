
import logging

import sys
import os
from datetime import date, datetime
import logging


from flask import (
    Flask,
    request,
    jsonify,
    redirect,
    render_template,
    url_for,
    abort
)
app = Flask(__name__)

logfilename = 'my-flask-app-log.log'
LOG_LEVEL = 'INFO'
LOG_FILE = logfilename

try:
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(sys.stdout),
        ],
        level=LOG_LEVEL
    )
except IOError as err:
  logger.error(
        f'message="Unable to open log file {LOG_FILE} error="{err}"')
  sys.exit(1)


@app.route('/')
def index():
    data = '<h1>Hello from Flask</h1>'
    return render_template('index.html',data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5057)
