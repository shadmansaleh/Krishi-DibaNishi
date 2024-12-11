from flask import Blueprint, jsonify

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/crop-suggestions", methods=["GET"])
def get_crop_suggestions():
    crops = ["Wheat", "Rice", "Corn", "Soybeans"]
    return jsonify({"crops": crops})

@api.route("/weather", methods=["GET"])
def get_weather_prediction():
    weather = {"temperature": "30°C", "humidity": "60%"}
    return jsonify(weather)

@api.route("/market-prices", methods=["GET"])
def get_market_prices():
    prices = {"Wheat": 20, "Rice": 15, "Corn": 25}
    return jsonify(prices)
