# app.py
from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)
@app.route('/')
def home():
    return 'Welcome to the Diet Recommendation API!'

from flask import jsonify  # Add this import at the top if not already there

@app.route('/recommend', methods=['GET'])
def recommend():
    sample_diet = {
        "diet": "Balanced",
        "calories": 2000,
        "meals": [
            "Breakfast: Oatmeal with fruits",
            "Lunch: Grilled chicken with quinoa",
            "Snack: Mixed nuts",
            "Dinner: Veggie stir fry with tofu"
        ]
    }
    return jsonify(sample_diet)



# Load food data from CSV (dummy data for example)
foods = pd.DataFrame({
    'meal': ['Oats with fruits', 'Grilled chicken salad', 'Paneer curry', 'Vegetable soup'],
    'type': ['veg', 'non-veg', 'veg', 'veg'],
    'health_tags': ['low sugar', 'high protein', 'low fat', 'diabetic friendly']
})

# Calorie estimation function
def calculate_calories(age, weight, height, gender, activity_level, goal):
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_multiplier = {
        'low': 1.2,
        'medium': 1.55,
        'high': 1.9
    }
    tdee = bmr * activity_multiplier.get(activity_level.lower(), 1.2)

    if goal == 'weight loss':
        tdee -= 500
    elif goal == 'weight gain':
        tdee += 500

    return round(tdee)

# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    required_fields = ['age', 'weight', 'height', 'gender', 'activity_level', 'goal', 'dietary_pref', 'health_issues']

    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing input fields'}), 400

    calories = calculate_calories(data['age'], data['weight'], data['height'],
                                  data['gender'], data['activity_level'], data['goal'])

    filtered_foods = foods[foods['type'] == data['dietary_pref']]

    # Simple filtering by health issues
    recommendations = filtered_foods[filtered_foods['health_tags'].str.contains(
        '|'.join(data['health_issues']), case=False, na=False)]

    return jsonify({
        'daily_calorie_target': calories,
        'recommended_meals': recommendations['meal'].tolist()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


