
# 🏋️‍♂️ Workout Plan Recommender

نظام توصية بسيط ومخصص يقدم خطط تمارين رياضية بناءً على أهداف المستخدم، تاريخ تمارينه السابقة، وأي إصابات صحية يعاني منها.

---

## 📌 فكرة المشروع

يعتمد هذا المشروع على **Rule-Based Recommendation System** لاقتراح التمارين المناسبة لكل مستخدم حسب:

- 🎯 أهدافه (مثل: خسارة الوزن، بناء العضلات)
- 📋 تمارينه السابقة
- ⚠️ الإصابات أو المشاكل الصحية

---

## 🧠 مثال لبيانات المستخدم

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
├── app.py                # Flask Web App
├── recommender.py        # Rule-Based Recommendation Logic
├── user.json             # Sample User Data
│
├── templates/
│   └── index.html        # Main HTML Page (Bootstrap UI)
│
├── static/
│   └── styles.css        # Custom Styles (if needed)
│
└── README.md             # Project Documentation
```

---

## 💻 How to Run Locally

### ⚙️ 1. Clone the repository
```bash
git clone https://github.com/your-username/workout-recommender.git
cd workout-recommender
```

### 🐍 2. Install dependencies
```bash
pip install flask
```

### 🚀 3. Run the web app
```bash
python app.py
```

### 🌍 4. Open in your browser
Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🎥 Web Demo

📺 **واجهة المستخدم التفاعلية:**

[▶️ شاهد الفيديو](https://user-images.githubusercontent.com/your-username/your-demo-video.mp4)

*(ارفع الفيديو على GitHub أو YouTube وخد الرابط المباشر واستبدل اللينك 👆)*

---

## 🧪 مثال ناتج (في الكونسول)

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

## 🔮 أفكار تطوير مستقبلية

- استخدام خوارزميات Machine Learning لتقديم توصيات ذكية
- حفظ سجل التمارين للمستخدمين
- دعم أكثر للغة العربية في التوصيات
- إضافة خاصية حساب مستوى اللياقة البدنية الحالي للمستخدم

---

## 🧑‍💻 المطور

- 👤 أحمد مازون  
- 🔗 [GitHub: ahmedmazoon](https://github.com/ahmedmazoon)

---

## 📄 الرخصة

مشروع مفتوح المصدر لأغراض تعليمية فقط.
