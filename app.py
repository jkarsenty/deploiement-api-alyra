from flask import Flask, jsonify, request
from model import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Alyra Deployment API!"

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "API is running smoothly."})

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input, 'text' field is required."}), 400

    text = data['text']
    result = analyze_sentiment(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)