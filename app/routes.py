from flask import Blueprint, render_template, request
import pickle
import numpy as np
import os

main = Blueprint('main', __name__)

model_path = os.path.join("app", "model", "churn_model.pkl")
model = pickle.load(open(model_path, "rb"))

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/predict', methods=['POST'])
def predict():
    try:
        tenure = float(request.form['tenure'])
        monthly = float(request.form['monthly_charges'])
        total = float(request.form['total_charges'])

        data = np.array([[tenure, monthly, total]])

        prediction = model.predict(data)[0]
        prob = model.predict_proba(data)[0][1]

        if prediction == 1:
            result = f"⚠️ High Risk: Customer likely to churn ({round(prob*100,2)}%)"
        else:
            result = f"✅ Low Risk: Customer likely to stay ({round(prob*100,2)}%)"

        return render_template("result.html", result=result)

    except Exception as e:
        return f"Error: {str(e)}"