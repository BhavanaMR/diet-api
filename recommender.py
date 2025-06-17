# recommender.py
from models import UserProfile

def calculate_bmr(user):
    if user.gender.lower() == 'male':
        return 10 * user.weight + 6.25 * user.height - 5 * user.age + 5
    else:
        return 10 * user.weight + 6.25 * user.height - 5 * user.age - 161

def calculate_tdee(bmr, activity_level):
    factors = {'low': 1.2, 'medium': 1.55, 'high': 1.9}
    return bmr * factors.get(activity_level.lower(), 1.2)

def recommend_diet(data):
    user = UserProfile(**data)
    bmr = calculate_bmr(user)
    tdee = calculate_tdee(bmr, user.activity_level)

    if user.goal == "weight loss":
        target_calories = tdee - 500
    elif user.goal == "weight gain":
        target_calories = tdee + 500
    else:
        target_calories = tdee

    return {
        "BMR": round(bmr, 2),
        "TDEE": round(tdee, 2),
        "Target Calories": round(target_calories, 2),
        "Suggested Meals": {
            "Breakfast": ["Oats", "Banana", "Almond milk"],
            "Lunch": ["Brown Rice", "Tofu curry", "Salad"],
            "Dinner": ["Quinoa", "Lentil soup", "Cucumber"]
        }
    }

