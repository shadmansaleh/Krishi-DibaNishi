from flask import Blueprint, jsonify, request
import traceback
from app.models import Prices
from app.extensions import db
import requests
import os

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/crop-suggestions", methods=["GET"])
def get_crop_suggestions():
    crops = ["Wheat", "Rice", "Corn", "Soybeans"]
    return jsonify({"crops": crops})

@api.route("/market-prices", methods=["GET"])
def get_market_prices():
    prices_data = Prices.query.all()
    prices = [
        {
            "id": item.id,
            "crop": item.crop,
            "region": item.region,
            "price_per_kg": item.price_per_kg,
            "price_per_kg_retail": item.price_per_kg_retail
        }
        for item in prices_data
    ]
    return jsonify(prices)

# Get a specific price
@api.route('/market-prices/<int:id>', methods=['GET'])
def get_price(id):
    price = Prices.query.get_or_404(id)
    return jsonify({
        'id': price.id,
        'crop': price.crop,
        'region': price.region,
        'price_per_kg': price.price_per_kg,
        'price_per_kg_retail': price.price_per_kg_retail
    })

# Add a new price
@api.route('/market-prices', methods=['POST'])
def add_price():
    try:
        data = request.get_json()
        price = Prices(
            crop=data['crop'],
            region=data['region'],
            price_per_kg=data['price_per_kg'],
            price_per_kg_retail=data['price_per_kg_retail']
        )
        db.session.add(price)
        db.session.commit()
        return jsonify({'message': 'Price added successfully!'}), 201
    except Exception as e:
        print(f"Error: {e}")
        print("Stack Trace:")
        print(traceback.format_exc())
        return jsonify({'message': 'Failed to add price'}), 500

# Update an existing price
@api.route('/market-prices/<int:id>', methods=['PUT'])
def update_price(id):
    data = request.get_json()
    price = Prices.query.get_or_404(id)
    price.crop = data['crop']
    price.region = data['region']
    price.price_per_kg = data['price_per_kg']
    price.price_per_kg_retail = data['price_per_kg_retail']
    db.session.commit()
    return jsonify({'message': 'Price updated successfully!'})

# Delete a price
@api.route('/market-prices/<int:id>', methods=['DELETE'])
def delete_price(id):
    price = Prices.query.get_or_404(id)
    db.session.delete(price)
    db.session.commit()
    return jsonify({'message': 'Price deleted successfully!'})

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
