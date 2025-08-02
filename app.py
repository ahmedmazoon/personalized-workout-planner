from flask import Flask, render_template, request
import json
from recommender import generate_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = None
    if request.method == "POST":
        goals = request.form.get("goals", "")
        past = request.form.get("past", "")
        injuries = request.form.get("injuries", "")
        recommendations = generate_recommendations(goals, past, injuries)
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    
    with open("user.json") as f:
        users = json.load(f)
        for user in users:
            print(f"\nUser {user['user_id']} Recommendation:")
            recs = generate_recommendations(user["goal"], user["past_workouts"], user["injuries"])
            for r in recs:
                print(" -", r)

    app.run(debug=True)

