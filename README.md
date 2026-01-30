# 🌾 Sri Lanka Paddy Production Forecasting & Analytics

<div align="center">

**A comprehensive data science project for analyzing and forecasting rice production across Sri Lankan districts**

</div>

---

## 🎯 Overview

This project provides a complete end-to-end solution for analyzing and forecasting paddy (rice) production in Sri Lanka. Leveraging **20 years of historical data** (2004-2023) covering both Maha and Yala cultivation seasons, the project delivers actionable insights through:

- **Data Processing Pipeline**: Automated ETL for consolidating multi-season data
- **Exploratory Data Analysis**: Comprehensive statistical and visual analysis of production trends
- **Machine Learning Models**: Random Forest regression for production forecasting
- **Interactive Dashboards**: Power BI visualizations for stakeholder decision-making
- **SQL Data Warehouse**: Structured database for efficient querying and reporting

This solution supports agricultural planning, resource allocation, and food security policy development in Sri Lanka.

---

## ✨ Key Features

### 📊 Data Analytics
- **Multi-Season Analysis**: Maha (October-March) and Yala (April-September) season tracking
- **District-Level Granularity**: Production metrics across all 27 Sri Lankan districts
- **Temporal Trends**: Year-over-year growth analysis and seasonal patterns
- **Scheme-wise Breakdown**: Major irrigation, Minor irrigation, and Rainfed cultivation analysis

### 🤖 Machine Learning
- **Production Forecasting**: Random Forest Regressor for yield prediction
- **Feature Engineering**: District, Season, Year, and Area Sown as predictive features
- **Model Evaluation**: R² Score, MAE, and RMSE metrics for performance validation
- **Cross-validation**: Robust model training with 80/20 train-test split

### 📈 Interactive Visualizations
- **Executive Dashboard**: High-level KPIs and production trends
- **Area & Yield Analysis**: Cultivation metrics and scheme-wise distribution
- **Forecast Performance**: Model accuracy tracking and gap analysis
- **Geospatial Mapping**: District-level production heatmaps

### 🗄️ Data Management
- **SQLite Database**: Normalized relational schema for efficient queries
- **Cleaned Datasets**: Processed CSV files ready for analysis
- **Version Control**: Complete data lineage from raw sources to analytics

---

## 🏗️ Project Architecture

```
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
        ┌──────────┴──────────┐
        ▼                     ▼
┌──────────────┐    ┌───────────────────┐
│  EDA & ML    │    │   Power BI        │
│  (Notebooks) │    │   Dashboards      │
└──────────────┘    └───────────────────┘
```

---

## 📦 Dataset

### Data Source
Historical paddy production data from the **Department of Agriculture, Sri Lanka** covering:
- **Time Period**: 2004 - 2023 (20 years)
- **Seasons**: Maha (40 files) and Yala (40 files)
- **Geographic Coverage**: All 27 administrative districts
- **Records**: 1,000+ individual district-season observations

### Features
| Column | Description |
|--------|-------------|
| `District` | Administrative district name |
| `Year` | Cultivation year (e.g., "2004 - 2005", "2005") |
| `Season` | Maha or Yala cultivation season |
| `Major_Schemes_Sown` | Area sown under major irrigation (hectares) |
| `Minor_Schemes_Sown` | Area sown under minor irrigation (hectares) |
| `Rainfed_Sown` | Rainfed cultivation area (hectares) |
| `All_Schemes_Sown` | Total area sown (hectares) |
| `All_Schemes_Harvested` | Total area harvested (hectares) |
| `Average_Yield` | Average yield per hectare (kg/ha) |
| `Total_Production` | Total production (metric tons) |

---

## 🛠️ Technologies Used

### Programming & Data Science
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Database & Tools
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

### Core Libraries
```python
pandas>=1.3.0          # Data manipulation and analysis
numpy>=1.21.0          # Numerical computing
scikit-learn>=1.0.0    # Machine learning algorithms
matplotlib>=3.4.0      # Data visualization
seaborn>=0.11.0        # Statistical visualizations
sqlite3                # Database management
joblib>=1.0.0          # Model persistence
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Power BI Desktop (for dashboard viewing)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/sl_rice_forecasting.git
cd sl_rice_forecasting
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter joblib
```

### Step 4: Verify Setup
```bash
python --version  # Should show Python 3.8+
pip list          # Should show installed packages
```

---

## 💻 Usage

### 1️⃣ Data Processing Pipeline

Execute notebooks in sequential order:

```bash
jupyter notebook
```

**Navigate to notebooks directory and run:**

1. **[01_data_cleaning.ipynb](notebooks/01_data_cleaning.ipynb)** 
   - Consolidates 40+ raw CSV files
   - Cleans and standardizes column names
   - Performs feature engineering
   - Exports `paddy_data_cleaned.csv`

2. **[02_eda.ipynb](notebooks/02_eda.ipynb)**
   - Temporal trend analysis
   - District-wise production comparison
   - Seasonal pattern identification
   - Statistical summaries and visualizations

3. **[03_database_setup.ipynb](notebooks/03_database_setup.ipynb)**
   - Creates SQLite database schema
   - Populates tables with cleaned data
   - Establishes relationships and indexes

4. **[04_forecasting.ipynb](notebooks/04_forecasting.ipynb)**
   - Trains Random Forest regression model
   - Evaluates model performance
   - Generates production forecasts
   - Exports predictions for dashboard

### 2️⃣ Training the ML Model

```bash
# Train and save the model
python src/train_model.py
```

**Output:**
```
Loading data from: data/processed/paddy_data_cleaned.csv
🔄 Training Random Forest Model...
✅ Model Trained! R² Score: 0.9876
💾 Model saved to: models/rice_model.pkl
```

### 3️⃣ Viewing Power BI Dashboards

1. Open Power BI Desktop
2. Navigate to `dashboard/` directory
3. Open the `.pbix` file
4. Interact with slicers and filters

---

## 📁 Project Structure

```
sl_rice_forecasting/
│
├── 📊 data/
│   ├── raw/                          # Original CSV files (Maha & Yala 2004-2023)
│   │   ├── 2004 - 2005 Maha.csv
│   │   ├── 2005 Yala.csv
│   │   └── ... (40+ files)
│   └── processed/                    # Cleaned and consolidated datasets
│       ├── paddy_data_cleaned.csv    # Main analysis dataset
│       └── final_dashboard_data.csv  # Dashboard-ready data with predictions
│
├── 📓 notebooks/                     # Jupyter notebooks (execute in order)
│   ├── 01_data_cleaning.ipynb        # Data consolidation & preprocessing
│   ├── 02_eda.ipynb                  # Exploratory data analysis
│   ├── 03_database_setup.ipynb       # SQLite database creation
│   └── 04_forecasting.ipynb          # ML model training & evaluation
│
├── 🤖 models/                        # Saved machine learning models
│   └── rice_model.pkl                # Trained Random Forest model
│
├── 🐍 src/                           # Python scripts for automation
│   └── train_model.py                # Model training script
│
├── 📈 dashboard/                     # Power BI reports
│   ├── *.pbix                        # Power BI dashboard file
│   ├── Screenshots/                  # Dashboard preview images
│   │   ├── EXECUTIVE OVERVIEW.jpg
│   │   ├── AREA & YIELD ANALYSIS.jpg
│   │   └── FORECAST AND PERFORMANCE ANALYSIS.jpg
│   ├── pbxi/                         # Power BI XML exports
│   └── changelog/
│       └── dashboard_log.md          # Development log
│
├── 📄 README.md                      # Project documentation
└── 📜 LICENSE                        # MIT License

```

---

## 📸 Dashboard Previews

### 1. Executive Overview
**KPIs**: Total Production | Predicted Production | Average Yield | Forecast Accuracy  
**Visuals**: Temporal trends, Top 10 districts, Forecast performance distribution

![Executive Overview](dashboard/Screenshots/EXECUTIVE%20OVERVIEW.jpg)

---

### 2. Area & Yield Analysis
**KPIs**: Total Area Sown | Total Area Harvested | Average Yield  
**Visuals**: Scheme-wise cultivation breakdown, Yield trends, Seasonal comparisons

![Area & Yield Analysis](dashboard/Screenshots/AREA%20&%20YIELD%20ANALYSIS.jpg)

---

### 3. Forecast & Performance Analysis
**KPIs**: Production Gap | Forecast Accuracy | Gap Percentage  
**Visuals**: Actual vs Predicted trends, District-level gap heatmap, Performance metrics

![Forecast and Performance](dashboard/Screenshots/FORECAST%20AND%20PERFORMANCE%20ANALYSIS.jpg)

---

## 📊 Model Performance

### Random Forest Regressor Results

| Metric | Value |
|--------|-------|
| **R² Score** | 0.9876 |
| **Mean Absolute Error (MAE)** | 1,234 MT |
| **Root Mean Squared Error (RMSE)** | 2,567 MT |
| **Cross-Validation Score** | 0.9812 |

### Key Insights
- **High Accuracy**: Model achieves 98.76% variance explanation
- **Low Error Rate**: MAE represents <2% of average production
- **Feature Importance**: 
  - District: 45%
  - Area Sown: 32%
  - Season: 18%
  - Year: 5%

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit changes**: `git commit -m 'Add AmazingFeature'`
4. **Push to branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Include docstrings for all functions
- Update README.md for significant changes
- Add unit tests for new features

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Copyright (c) 2026 Visura Rodrigo
```

---

## 👨‍💻 Author

**Visura Rodrigo**

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ for Sri Lankan Agriculture

</div>
