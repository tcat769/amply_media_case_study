"""Blueprint for all weather related endpoints."""

import logging
from flask import request, jsonify, Blueprint
from blueprints.weather import weather_utils

logger = logging.getLogger(__name__)
weather_blueprint = Blueprint("weather", "weather_blueprint")


@weather_blueprint.route("/weather", methods=["GET"])
def get_local_weather():
    """GET endpoint that retrieves a local weather report for the next three days.

    Returns:
        JSON: A JSON response that contains the city, state, and three day weather report detailing
            the expected weather conditions and the temperature high and low.
    """
    returnable = {}
    aws_weather_json = weather_utils.get_weather_from_aws()

    returnable['city'] = weather_utils.get_city_from_aws_json(aws_weather_json)
    returnable['state'] = weather_utils.get_state_from_aws_json(aws_weather_json)
    logger.info(f"{request.remote_addr} - Request for Weather made from {returnable.get('city')}, {returnable.get('state')}.")
    returnable['weather'] = weather_utils.get_three_day_weather_report(aws_weather_json)

    return jsonify(returnable)
