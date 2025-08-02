
# 🏋️‍♂️ Workout Plan Recommender

A simple rule-based system that recommends personalized workout plans based on user goals, workout history, and existing injuries.

---

## 📌 Project Overview

This project uses a **Rule-Based Recommendation System** to generate suitable workout suggestions for each user based on:

- 🎯 **Goals** (e.g., lose weight, build muscle)
- 📋 **Past workouts**
- ⚠️ **Injuries or health conditions**

---

## 🧠 Sample User Data

```json
{
  "user_id": 1,
  "goal": "lose weight",
  "past_workouts": ["cardio", "hiit"],
  "injuries": ["knee"]
}
```

---

## 🗂️ Project Structure

```
Workout-Recommender/
│
├── app.py                # Flask web application
├── recommender.py        # Rule-based recommendation logic
├── user.json             # Sample user data
│
├── templates/
│   └── index.html        # Main Bootstrap UI
│
├── static/
│   └── style.css         # Optional custom styles
│
└── README.md             # Project documentation
```

---

## 💻 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/workout-recommender.git
cd workout-recommender
```

### 2️⃣ Install Dependencies

```bash
pip install flask
```

### 3️⃣ Run the Flask App

```bash
python app.py
```

### 4️⃣ Open in Browser

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🎥 Web Demo

📺 **Interactive Web Interface:**

[▶️ Watch Demo Video](https://user-images.githubusercontent.com/your-username/your-demo-video.mp4)

> Replace the link above with your actual video URL (GitHub, YouTube, etc.)

---

## 🧪 Example Console Output

```text
User 1 Recommendation:
 - Swimming
 - Upper body workouts
 - Low-impact cycling

User 2 Recommendation:
 - Deadlifts
 - Push-pull workout
 - Leg day plan
```

---

## 👨‍💻 Developer

- **Ahmed Mazoon**
- [GitHub Profile](https://github.com/ahmedmazoon)

---
