from flask import Blueprint, jsonify, request
import requests
import os

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/crop-suggestions", methods=["GET"])
def get_crop_suggestions():
    crops = ["Wheat", "Rice", "Corn", "Soybeans"]
    return jsonify({"crops": crops})

@api.route("/market-prices", methods=["GET"])
def get_market_prices():
    prices = {"Wheat": 20, "Rice": 15, "Corn": 25}
    return jsonify(prices)

@api.route('/weather', methods=['POST'])
def get_weather():
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    OPENWEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'
    data = request.get_json()
    location = data.get('location')

    if location == "current":
        location = "Chittagong"

    try:
        response = requests.get(OPENWEATHER_URL, params={
            'q': location,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric'
        })
        response.raise_for_status()
        weather_data = response.json()

        result = {
            'location': weather_data.get('name'),
            'description': weather_data['weather'][0]['description'].capitalize(),
            'temperature': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
            'pressure': weather_data['main']['pressure'],
            'cloudiness': weather_data['clouds']['all'],
            'sunrise': weather_data['sys']['sunrise'],
            'sunset': weather_data['sys']['sunset'],
            'icon': weather_data['weather'][0]['icon']
        }
        return jsonify(result)

    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Unable to fetch weather data.'}), 500
