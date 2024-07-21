from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Vodka Collection API"})

@app.route('/vodkas', methods=['GET'])
def get_vodkas():
    return jsonify([
        {"name": "Vodka A", "origin": "Russia", "alcohol_content": 40},
        {"name": "Vodka B", "origin": "Poland", "alcohol_content": 45}
    ])

if __name__ == '__main__':
    app.run(debug=True)
