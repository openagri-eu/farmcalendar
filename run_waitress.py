#!/usr/bin/env python
import logging
import warnings
import os

from waitress import serve
from farm_calendar.wsgi import application

host = os.getenv('APP_HOST', '0.0.0.0')
port = int(os.getenv('APP_PORT', '9000'))
LOGGIN_LEVEL = os.getenv('LOGGIN_LEVEL', 'DEBUG')


logging.basicConfig(filename='logs/waitress.log', level=getattr(logging, LOGGIN_LEVEL))

warnings.filterwarnings("ignore")

serve(application, host=host, port=port)
