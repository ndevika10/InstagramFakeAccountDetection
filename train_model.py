import pickle
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load dataset (Ensure the CSV file exists and has the required columns)
data = pd.read_csv("D:\\final year project attempt\IJECE_df_train.csv")

# Feature selection and preprocessing
features = ['nmedia', 'nfollower', 'nfollowing', 'pic']
X = data[features]
y = data['fake']  # 1 for real, 0 for fake

# Normalize numerical features
scaler = StandardScaler()
X[features] = scaler.fit_transform(X[features])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
xgb_model = XGBClassifier()
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)

# Print accuracy
print("XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))

# Save the trained model
with open("xgboost_model.pkl", "wb") as f:
    pickle.dump((xgb_model, scaler), f)

print("Model training completed and saved as xgboost_model.pkl")
