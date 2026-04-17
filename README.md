# 🚀 Customer Churn Prediction System (IBM Telco)

A modern **Machine Learning + Flask Web Application** that predicts whether a customer is likely to churn based on key telecom usage features.

Built using the **IBM Telco Customer Churn Dataset**, this project combines data science with a clean dashboard UI to deliver real-time predictions and business insights.

---

## 📊 Features

* 🔍 Real-time churn prediction
* 🤖 Machine Learning model (Random Forest)
* 📈 Visual insights (charts & trends)
* 🎨 Modern dashboard UI (Flask + CSS)
* 💡 Business recommendations based on prediction

---

## 🧠 Tech Stack

* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Frontend:** HTML, CSS, JavaScript
* **Visualization:** Matplotlib

---

## 📁 Project Structure

```
Customer Churn Prediction/
│
├── app/                # Flask application
├── data/               # Dataset
├── scripts/            # Model training
├── notebooks/          # EDA & analysis
├── run.py              # Entry point
└── requirements.txt
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd Customer-Churn-Prediction
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Train the Model

```
python scripts/train_model.py
```

---

### 4️⃣ Run the Application

```
python run.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📌 Input Features

* Tenure (Months)
* Monthly Charges
* Total Charges

---

## 📈 Model Details

* **Algorithm:** Random Forest Classifier
* **Accuracy:** ~75–82%
* **Target:** Churn (0 = No, 1 = Yes)

---

## 💡 Key Insights

* Customers with **low tenure** are more likely to churn
* **Higher monthly charges** increase churn probability
* Long-term engagement reduces churn risk

---

## 🎯 Future Improvements

* 📊 Interactive dashboards (Plotly)
* 🔐 User authentication system
* 🌍 Cloud deployment
* 📈 Multiple model comparison

---

## 👨‍💻 Author

Sandesh Somnath Naikwade

---

## ⭐ Acknowledgment

Dataset provided by **IBM Telco Customer Churn Dataset**

---

## 🧠 Note

This project is developed for educational purposes and demonstrates the integration of machine learning with web development.

---
