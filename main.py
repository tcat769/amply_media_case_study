"""Main entry point to the flask endpoint.  Configures the app to run locally."""

import requests_cache
from logging_utils.my_logger import setup_logger
from constants import LOG_FILE
from app.flask_app import flask_app
from blueprints.weather import weather_api

setup_logger(LOG_FILE)

requests_cache.install_cache('test_flask_app', expire_after=600)

flask_app.register_blueprint(weather_api.weather_blueprint)


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port='5002')
