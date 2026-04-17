import pandas as pd
import numpy as np
import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/raw/Telco_customer_churn.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Drop unnecessary columns
drop_cols = [
    'City', 'Zip Code', 'Lat Long', 'Latitude', 'Longitude',
    'Churn Score', 'CLTV', 'Churn Reason'
]
df.drop(columns=drop_cols, inplace=True)

# Convert Total Charges
df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
df.dropna(inplace=True)

# Select important features
features = ['Tenure Months', 'Monthly Charges', 'Total Charges']
X = df[features]

# Target
y = df['Churn Value']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))

# Save model
os.makedirs("app/model", exist_ok=True)
pickle.dump(model, open("app/model/churn_model.pkl", "wb"))

print("✅ Model trained & saved successfully!")