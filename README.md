
# 🏋️‍♂️ Personalized Workout Planner

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
git clone https://github.com/ahmedmazoon/personalized-workout-planner.git
cd personalized-workout-planner
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
 - Push-Pull Workout
 - Full-Body Circuits
 - Hiit
 - Machine-Based Exercises
 - Swimming

User 2 Recommendation:
 - Cardio Circuits
 - Push-Pull Workout
 - Full-Body Circuits
 - Hiit
 - Machine-Based Exercises

User 3 Recommendation:
 - Cardio Circuits
 - Push-Pull Workout
 - Full-Body Circuits
 - Hiit
 - Machine-Based Exercises
```

---

## 🖼️ Web Deployment Preview

### 🏠 Home Page
<p align="center">  
  <img src="image/home.png" width="500" alt="Confusion Matrix">  
</p>

### ✅ Console and Web Output
<p align="center">  
  <img src="image/recommendations.png" width="500" alt="Accuracy Plot">  
</p>

---
## ✅ Features

- 🧠 Rule-Based Workout Recommendations  
- 📂 Reads user preferences from a JSON file  
- ⚖️ Scores each workout suggestion based on relevance  
- 🖥️ Flask web interface with Bootstrap styling  
- 🔄 Dynamic display of personalized workout plans  
- ⚠️ Injury-aware suggestions (avoids harmful exercises)  
- 🧪 Console + Web output for testing and validation 
---
## 👨‍💻 Developer

- **Ahmed Mazoon**
- [GitHub Profile](https://github.com/ahmedmazoon)

---
