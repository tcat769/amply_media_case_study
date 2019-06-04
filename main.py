#!/usr/bin/env python
import logging
from flask import Flask
from flask_restful import Api
from my_logger import my_logger
from request_weather import request_weather

# initialize logger
logger = logging.getLogger('amcs')

# create flask and api objects
amcs_app = Flask('amcs_app')
amcs_api = Api(amcs_app)

# add our weather resource
amcs_api.add_resource(request_weather.Weather, '/weather')

if __name__ == '__main__':
     amcs_app.run(host='0.0.0.0', port='5002')
