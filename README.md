
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

📺 **Interactive User Interface:**

▶️ [Watch Demo Video](https://drive.google.com/file/d/1wtC2V7snp0X5jTs77S9K8pw8l-Q4ISyh/view?usp=sharing)

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

## 🖼️ Web Deployment Preview

### 🏠 Home Page
![Home Page](https://raw.githubusercontent.com/ahmedmazoon/personalized-workout-planner/main/image/Screenshot 2025-08-03 012807.png)

### ✅ Console and Web Output
![Recommendations](https://raw.githubusercontent.com/ahmedmazoon/personalized-workout-planner/main/image/recommendations.png)
---
## 👨‍💻 Developer

- **Ahmed Mazoon**
- [GitHub Profile](https://github.com/ahmedmazoon)

---
