import logging
import requests
from constants import WEATHER_URL

logger = logging.getLogger(__name__)


def get_weather_from_aws():
    """Gets the local weather information from AWS.

    Returns:
        dict: A dictionary representation of the json returned from AWS weather endpoint.
    """
    response = requests.get(WEATHER_URL)
    logger.info(f"Used cache? {response.from_cache}")
    if response.status_code != 200:
        raise Exception("Unable to get local weather from AWS.")
    return response.json()


def get_city_from_aws_json(aws_weather_json: dict):
    """Retrieves the local city name from the AWS returned JSON.

    Args:
        aws_weather_json: The JSON dictionary returned from the AWS weather endpoint.

    Returns:
        str: The name of the city that the weather JSON is for.
    """
    return aws_weather_json.get('today', {}).get('city')


def get_state_from_aws_json(aws_weather_json: dict):
    """Retrieves the local state name from the AWS returned JSON.

    Args:
        aws_weather_json: The JSON dictionary returned from the AWS weather endpoint.

    Returns:
        str: The name of the state that the weather JSON is for.
    """
    return aws_weather_json.get('today', {}).get('state')


def get_three_day_weather_report(aws_weather_json: dict):
    """Retrieves the local weather for the next three days.

    Args:
        aws_weather_json: The JSON dictionary returned from the AWS weather endpoint.

    Returns:
        dict: A dictionary of the next including the description, high, and low for each.
    """
    daily_list = aws_weather_json.get('daily')[:3]

    daily_weather_dict = {}
    for day in daily_list:
        daily_weather_dict[day.get('utcTime')] = {
            'description': day.get('description'),
            'high': day.get('highTemperature'),
            'low': day.get('lowTemperature'),
        }

    return daily_weather_dict
