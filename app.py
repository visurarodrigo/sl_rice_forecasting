import gradio as gr
import joblib
import pandas as pd

# 1. Load the model and the saved column names
model = joblib.load('models/rice_model.pkl')
model_columns = joblib.load('models/model_columns.pkl')

# 2. Define the prediction function
def predict_paddy_production(year, season, district, area_sown):
    # Create a DataFrame from user inputs
    input_data = pd.DataFrame({
        'Year': [year],
        'Season': [season],
        'District': [district],
        'All_Schemes_Sown': [area_sown]
    })
    
    # Apply the exact same One-Hot Encoding we used in training
    input_encoded = pd.get_dummies(input_data, drop_first=True)
    
    # Align the input columns with the model's expected columns
    # This adds missing columns as 0 and drops any extra ones so the model doesn't crash
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)
    
    # Make the prediction
    prediction = model.predict(input_encoded)[0]
    
    # Return a nicely formatted string
    return f"{prediction:,.2f} Metric Tons"

# 3. Build the Gradio Interface
# A list of Sri Lankan districts for the dropdown menu
districts = ['Colombo', 'Gampaha', 'Kalutara', 'Kandy', 'Matale', 'Nuwara Eliya', 
             'Galle', 'Matara', 'Hambantota', 'Jaffna', 'Kilinochchi', 'Mullaitivu', 
             'Mannar', 'Vavuniya', 'Trincomalee', 'Batticaloa', 'Ampara', 
             'Kurunegala', 'Puttalam', 'Anuradhapura', 'Polonnaruwa', 
             'Badulla', 'Monaragala', 'Ratnapura', 'Kegalle']

demo = gr.Interface(
    fn=predict_paddy_production,
    inputs=[
        gr.Number(label="Year (e.g., 2023)", value=2023),
        gr.Dropdown(choices=["Maha", "Yala"], label="Season", value="Maha"),
        gr.Dropdown(choices=districts, label="District", value="Colombo"),
        gr.Number(label="Total Area Sown (All Schemes) in Hectares", value=1000)
    ],
    outputs=gr.Textbox(label="Forecasted Total Paddy Production"),
    title="🌾 Sri Lanka Paddy Production Forecaster",
    description="Predict the total paddy production based on the year, season, district, and area sown using a Random Forest machine learning model."
)

# 4. Launch the app
if __name__ == "__main__":
    demo.launch()