from flask import Blueprint, request, jsonify
import pickle  # Assuming you're using a pickle model

predict_bp = Blueprint('predict', __name__)

# Load your model (adjust the path as needed)
with open('app/rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

@predict_bp.route('/predict-crop', methods=['POST'])
def predict_crop():
    data = request.get_json()
    features = [
        float(data['nitrogen']),
        float(data['phosphorus']),
        float(data['potassium']),
        float(data['temperature']),
        float(data['humidity']),
        float(data['ph']),
        float(data['rainfall'])
    ]

    # Make prediction
    prediction = model.predict([features])
    crop = prediction[0]

    return jsonify({'crop': crop})
