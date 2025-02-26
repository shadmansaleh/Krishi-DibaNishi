from flask import Blueprint, request, jsonify
import pickle
import numpy as np

predict_bp = Blueprint('predict', __name__)

# Load the trained model
with open('app/rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the saved scaler
with open('app/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Mapping of crops to their Bangla names
crop_mapping = {
    'rice': 'চাল / ধান',
    'maize': 'ভুট্টা',
    'jute': 'পাট',
    'cotton': 'তুলা',
    'coconut': 'নারকেল',
    'papaya': 'পেঁপে',
    'orange': 'কমলা',
    'apple': 'আপেল',
    'muskmelon': 'খরমুজ',
    'watermelon': 'তরমুজ',
    'grapes': 'আঙুর',
    'mango': 'আম',
    'banana': 'কলা',
    'pomegranate': 'ডালিম / আনার',
    'lentil': 'মসুর ডাল',
    'blackgram': 'কালো মটর ডাল (মাষকলাই)',
    'mungbean': 'মুগ ডাল',
    'mothbeans': 'মট ডাল',
    'pigeonpeas': 'অড়হর ডাল',
    'kidneybeans': 'রাজমা',
    'chickpea': 'ছোলা',
    'coffee': 'কফি'
}

@predict_bp.route('/predict-crop', methods=['POST'])
def predict_crop():
    data = request.get_json()
    
    # Extract and convert input features
    features = np.array([[
        float(data['nitrogen']),
        float(data['phosphorus']),
        float(data['potassium']),
        float(data['temperature']),
        float(data['humidity']),
        float(data['ph']),
        float(data['rainfall'])
    ]])

    # Scale the input using the loaded scaler
    features_scaled = scaler.transform(features)

    # Make prediction
    prediction = model.predict(features_scaled)
    crop = prediction[0]
    
    # Get the Bangla crop name
    bangla_crop = crop_mapping.get(crop.lower(), "Unknown crop")
    
    return jsonify({'crop': bangla_crop})
