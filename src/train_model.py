import pandas as pd
import numpy as np
import os
import joblib  # Standard way to save models
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Setup Paths
# We use abspath to make sure it works no matter where you run the command from
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'paddy_data_cleaned.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'rice_model.pkl') # We will create a models folder

def load_and_preprocess(path):
    """Loads data and performs One-Hot Encoding"""
    print(f"Loading data from: {path}")
    df = pd.read_csv(path)
    
    features = ['Year', 'Season', 'District', 'All_Schemes_Sown']
    target = 'Total_Production'
    
    # One-Hot Encoding
    X = pd.get_dummies(df[features], drop_first=True)
    y = df[target]
    
    return X, y

def train():
    """Main execution function"""
    # Load Data
    if not os.path.exists(DATA_PATH):
        print(f"❌ Error: Data file not found at {DATA_PATH}")
        return

    X, y = load_and_preprocess(DATA_PATH)
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train
    print("🔄 Training Random Forest Model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    accuracy = model.score(X_test, y_test)
    print(f"✅ Model Trained! R² Score: {accuracy:.4f}")
    
    # Save Model
    # (Optional: create 'models' folder if it doesn't exist)
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"💾 Model saved to: {MODEL_PATH}")

if __name__ == "__main__":
    train()