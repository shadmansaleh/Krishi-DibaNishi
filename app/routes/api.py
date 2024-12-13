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
    # OpenWeather API configuration
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    OPENWEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
    FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast'

    data = request.get_json()
    location = data.get('location', 'Chittagong')

    try:
        # Request current weather data from OpenWeather API
        current_response = requests.get(OPENWEATHER_URL, params={
            'q': location,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric'
        })
        current_response.raise_for_status()
        current_weather = current_response.json()

        # Request forecast data from OpenWeather API
        forecast_response = requests.get(FORECAST_URL, params={
            'q': location,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric'
        })
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        # Extract current weather data
        current_result = {
            'location': current_weather.get('name'),
            'description': current_weather['weather'][0]['description'].capitalize(),
            'temperature': current_weather['main']['temp'],
            'humidity': current_weather['main']['humidity'],
            'wind_speed': current_weather['wind']['speed'],
            'pressure': current_weather['main']['pressure'],
            'cloudiness': current_weather['clouds']['all'],
            'sunrise': current_weather['sys']['sunrise'],
            'sunset': current_weather['sys']['sunset'],
            'icon': current_weather['weather'][0]['icon']
        }

        # Extract forecast data for the next 5 days
        daily_forecasts = []
        for i in range(0, len(forecast_data['list']), 8):  # 8 data points per day
            day_data = forecast_data['list'][i]
            daily_forecasts.append({
                'date': day_data['dt_txt'].split()[0],  # Extract date (YYYY-MM-DD)
                'description': day_data['weather'][0]['description'].capitalize(),
                'temperature': day_data['main']['temp'],
                'humidity': day_data['main']['humidity'],
                'wind_speed': day_data['wind']['speed'],
                'icon': day_data['weather'][0]['icon']
            })

        return jsonify({'current': current_result, 'forecast': daily_forecasts})

    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Unable to fetch weather data.'}), 500
