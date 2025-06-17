# app.py
from flask import Flask, request, jsonify
from recommender import recommend_diet
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_data = request.json
    result = recommend_diet(user_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

