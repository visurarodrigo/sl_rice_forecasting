
# 🌾 Sri Lanka Paddy Production Forecasting & Analytics

<div align="center">

**A comprehensive end-to-end data science project for analyzing and forecasting rice production across Sri Lankan districts.**

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Live%20App-blue)](https://huggingface.co/spaces/visurarodrigo/sl-paddy-forecaster)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

🔗 **Try the Live Interactive Forecasting App Here:** [Sri Lanka Paddy Forecaster](https://huggingface.co/spaces/visurarodrigo/sl-paddy-forecaster)

</div>

---

## 🎯 Overview

This project provides a complete end-to-end solution for analyzing and forecasting paddy (rice) production in Sri Lanka. Leveraging **20 years of historical data** (2004-2023) covering both Maha and Yala cultivation seasons, the project delivers actionable insights through:

- **Data Processing Pipeline**: Automated ETL for consolidating multi-season data.
- **Exploratory Data Analysis**: Comprehensive statistical and visual analysis of production trends.
- **Machine Learning Models**: Random Forest regression for production forecasting (R² = 0.95+).
- **Live Web Deployment**: Interactive Gradio UI hosted on Hugging Face Spaces for real-time predictions.
- **Interactive Dashboards**: Power BI visualizations for stakeholder decision-making.
- **SQL Data Warehouse**: Structured SQLite database for efficient querying and reporting.

This solution supports agricultural planning, resource allocation, and food security policy development in Sri Lanka.

---

## ✨ Key Features

### 🌐 Live Web Application
- **Interactive UI**: Built with Gradio for seamless user interaction.
- **Real-Time Forecasting**: Predicts total paddy production instantly based on user inputs (Year, Season, District, Area Sown).
- **Cloud Hosted**: Deployed publicly on Hugging Face Spaces for zero-friction access.

### 📊 Data Analytics
- **Multi-Season Analysis**: Maha (October-March) and Yala (April-September) season tracking.
- **District-Level Granularity**: Production metrics across all 27 Sri Lankan districts.
- **Temporal Trends**: Year-over-year growth analysis and seasonal patterns.
- **Scheme-wise Breakdown**: Major irrigation, Minor irrigation, and Rainfed cultivation analysis.

### 🤖 Machine Learning
- **Production Forecasting**: Random Forest Regressor for yield prediction.
- **Feature Engineering**: District, Season, Year, and Area Sown as predictive features.
- **Model Evaluation**: R² Score, MAE, and RMSE metrics for performance validation.
- **Robust Preprocessing**: Automated One-Hot Encoding and feature alignment for inference.

### 📈 Interactive Visualizations (Power BI)
- **Executive Dashboard**: High-level KPIs and production trends.
- **Area & Yield Analysis**: Cultivation metrics and scheme-wise distribution.
- **Forecast Performance**: Model accuracy tracking and gap analysis.
- **Geospatial Mapping**: District-level production heatmaps.

---

## 🏗️ Project Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    RAW DATA SOURCES                          │
│  (40+ CSV files: Maha & Yala seasons 2004-2023)            │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│               DATA CLEANING & PREPROCESSING                  │
│  • Consolidation  • Feature Engineering  • Normalization    │
└─────────────────────┬───────────────────────────────────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
┌──────────────────┐    ┌─────────────────────┐
│  SQLite Database │    │  Processed CSV Data │
│  (Relational)    │    │  (Analytics-Ready)  │
└────────┬─────────┘    └──────────┬──────────┘
         │                          │
         └─────────┬────────────────┘
                   │
    ┌──────────────┼──────────────┐
    ▼              ▼              ▼
┌────────┐   ┌──────────┐   ┌──────────────┐
│  EDA   │   │   ML     │   │   Power BI   │
│(Notebk)│   │ Training │   │  Dashboards  │
└────────┘   └────┬─────┘   └──────────────┘
                  │
                  ▼
         ┌─────────────────┐      ┌───────────────────────┐
         │  Gradio Web App │─────▶│  Hugging Face Spaces  │
         │   (app.py)      │      │  (Live Public URL)    │
         └─────────────────┘      └───────────────────────┘
```

---

## 🛠️ Technologies Used

### Programming & Data Science
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

### Deployment & Visualization
![Gradio](https://img.shields.io/badge/Gradio-FF7C00?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGdSURBVFhH7ZYxSwNBEEZji42VhYWNhY2Nfy3BxsZGEKy0sbAQ/BPGykLBT7CxEUQsLCxEMLFSsFLQD3wgB3tyt7O7c5Z7cMDOzXvvZnZndmH4xyhHcgxqQfYBvZBv5A75Ib4j75Ef5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5Jr4j7pEf5Bb5......)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 🚀 Installation & Local Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Power BI Desktop (for dashboard viewing)

### Step 1: Clone the Repository
```bash
git clone https://github.com/visurarodrigo/sl_rice_forecasting.git
cd sl_rice_forecasting
```

### Step 2: Create Virtual Environment & Install Dependencies
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

---

## 💻 Usage

### 1️⃣ Run the Live Web App (Gradio)
To run the interactive forecasting app locally:
```bash
python app.py
```
*This will launch a local web server (usually at `http://127.0.0.1:7860`). Open the URL in your browser to interact with the model.*

### 2️⃣ Data Processing & EDA Pipeline
Execute Jupyter notebooks in sequential order:
```bash
jupyter notebook
```
1. **[01_data_cleaning.ipynb](notebooks/01_data_cleaning.ipynb)**: Consolidates raw CSVs and exports `paddy_data_cleaned.csv`.
2. **[02_eda.ipynb](notebooks/02_eda.ipynb)**: Temporal trends, district comparisons, and visualizations.
3. **[03_database_setup.ipynb](notebooks/03_database_setup.ipynb)**: Creates and populates the SQLite database.
4. **[04_forecasting.ipynb](notebooks/04_forecasting.ipynb)**: Trains the ML model and generates forecasts.

### 3️⃣ Train the ML Model from Scratch
```bash
python src/train_model.py
```

### 4️⃣ Viewing Power BI Dashboards
1. Open Power BI Desktop.
2. Navigate to the `dashboard/` directory and open the `.pbix` file.

---

## 📁 Project Structure

```text
sl_rice_forecasting/
│
├── 📊 data/
│   ├── raw/                          # Original CSV files (Maha & Yala 2004-2023)
│   └── processed/                    # Cleaned and consolidated datasets
│       ├── paddy_data_cleaned.csv    
│       └── final_dashboard_data.csv  
│
├── 📓 notebooks/                     # Jupyter notebooks (execute in order)
│   ├── 01_data_cleaning.ipynb        
│   ├── 02_eda.ipynb                  
│   ├── 03_database_setup.ipynb       
│   └── 04_forecasting.ipynb          
│
├── 🤖 models/                        # Saved machine learning artifacts
│   ├── rice_model.pkl                # Trained Random Forest model
│   └── model_columns.pkl             # Expected feature columns for inference
│
├── 🐍 src/                           # Python scripts for automation
│   └── train_model.py                
│
├── 📈 dashboard/                     # Power BI reports and screenshots
│   ├── *.pbix                        
│   └── Screenshots/                  
│
├── 🌐 app.py                         # Gradio web application interface
├── 📜 requirements.txt               # Python dependencies for deployment
├── 📄 README.md                      
└── 📜 LICENSE                        
```

---

## 📸 Dashboard Previews

### 1. Executive Overview
**KPIs**: Total Production | Predicted Production | Average Yield | Forecast Accuracy  
![Executive Overview](dashboard/Screenshots/EXECUTIVE%20OVERVIEW.jpg)

### 2. Area & Yield Analysis
**KPIs**: Total Area Sown | Total Area Harvested | Average Yield  
![Area & Yield Analysis](dashboard/Screenshots/AREA%20&%20YIELD%20ANALYSIS.jpg)

### 3. Forecast & Performance Analysis
**KPIs**: Production Gap | Forecast Accuracy | Gap Percentage  
![Forecast and Performance](dashboard/Screenshots/FORECAST%20AND%20PERFORMANCE%20ANALYSIS.jpg)

---

## 📊 Model Performance

### Random Forest Regressor Results

| Metric | Value |
|--------|-------|
| **R² Score** | 0.9507 |
| **Mean Absolute Error (MAE)** | ~1,200 MT |
| **Root Mean Squared Error (RMSE)** | ~2,100 MT |

### Key Insights
- **High Accuracy**: Model achieves >95% variance explanation in production volume.
- **Feature Importance**: 
  - District: ~45%
  - Area Sown: ~32%
  - Season: ~18%
  - Year: ~5%

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ for Sri Lankan Agriculture by **Visura Rodrigo**

</div>


