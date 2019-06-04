import requests
import requests_cache
import logging
import pygeoip, json
from flask import request, jsonify
from flask_restful import Resource

# initialize logger
logger = logging.getLogger('amcs.request_weather')

# cache all requests for 5 minutes
requests_cache.install_cache('amcs', expire_after=600)

class Weather(Resource):
    def __init__(self):
        self.url = 'https://j9l4zglte4.execute-api.us-east-1.amazonaws.com/api/ctl/weather'

    def get(self):
        # make request unless it is cached
        returnable = {}
        r = requests.get(self.url)
        d = r.json()

        # get important information
        returnable['city'] = d.get('today').get('city')
        returnable['state'] = d.get('today').get('state')
        logger.info(f"{request.remote_addr} - Request for Weather made from {returnable.get('city')}, {returnable.get('state')}.")
        daily_list = d.get('daily')[:3]

        daily_weather_dict = {}
        for day in daily_list:
            daily_weather_dict[day.get('utcTime')] = {
                    'description': day.get('description'),
                    'high': day.get('highTemperature'),
                    'low': day.get('lowTemperature'),
                    }

        returnable['weather'] = daily_weather_dict

        return jsonify(returnable)


