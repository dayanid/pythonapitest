from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    data = {"message": "Welcome to the API!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
