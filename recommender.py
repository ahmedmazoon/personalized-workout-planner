import json

goal_map = {
    "lose weight": ["Swimming", "HIIT", "Running", "Cardio circuits", "Low-impact cycling", "Upper body workouts"],
    "build muscle": ["Deadlifts", "Push-pull workout", "Progressive overload plan", "Leg day plan", "Core training", "Machine-based exercises"],
    "improve fitness": ["Functional training", "CrossFit", "Full-body circuits", "Swimming", "Cardio circuits"]
}

injury_unsafe = {
    "knee": ["Running", "Deadlifts", "Leg day plan"],
    "shoulder": ["Push-pull workout", "CrossFit", "Upper body workouts"]
}

all_workouts = list(set(
    [w for lst in goal_map.values() for w in lst] +
    [w for lst in injury_unsafe.values() for w in lst]
))

def clean_list(input_string):
    if isinstance(input_string, list):
        return [i.strip().lower() for i in input_string]
    return [i.strip().lower() for i in input_string.split(",") if i.strip()]

def compute_score(workout, user_goals, past_workouts, injuries):
    score = 0

    for goal in user_goals:
        if workout in [w.lower() for w in goal_map.get(goal, [])]:
            score += 0.4
            break

    if not any(workout in [w.lower() for w in injury_unsafe.get(injury, [])] for injury in injuries):
        score += 0.3

    if workout.lower() not in past_workouts:
        score += 0.3

    return round(score, 2)

def generate_recommendations(goals_input, past_input, injuries_input):
    user_goals = clean_list(goals_input)
    past_workouts = clean_list(past_input)
    injuries = clean_list(injuries_input)

    if not user_goals:
        return [" Please enter at least one valid goal."]

    scored = []
    for workout in all_workouts:
        score = compute_score(workout, user_goals, past_workouts, injuries)
        if score > 0:
            scored.append((workout, score))

    sorted_workouts = sorted(scored, key=lambda x: x[1], reverse=True)
    return [w.title() for w, s in sorted_workouts[:5]]

