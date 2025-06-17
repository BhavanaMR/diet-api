# models.py
class UserProfile:
    def __init__(self, age, weight, height, gender, goal, activity_level, dietary_pref, health_issues):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.goal = goal
        self.activity_level = activity_level
        self.dietary_pref = dietary_pref
        self.health_issues = health_issues

