### Power BI Dashboard - Daily Log

#### Day 1 – Data Preparation & Modeling
- Imported `final_dashboard_data.csv` into Power BI
- Renamed all columns using professional, business-friendly naming conventions
- Created Start_Year, Season_Start_Date, and Season_Year_Label for time-based analysis
- Created a Date_Table and established relationships with Fact_Production
- Cleaned the data model by hiding technical fields
- Created core DAX measures:
  - Actual Production
  - Predicted Production
  - Production Gap
  - Forecast Accuracy
  - Average Yield
  - Forecast performance counts

#### Day 2 – Executive Overview Dashboard (Page 01)
- Designed Page 01: **Sri Lanka Paddy Production – Executive Overview**
- Created KPI cards for:
  - Actual Production
  - Predicted Production
  - Average Yield
  - Forecast Accuracy
- Built a line chart comparing Actual vs Predicted production over time
- Added a donut chart to visualize forecast performance distribution
- Created a bar chart highlighting the top 10 producing districts
- Added interactive slicers for Year, Season, and District
- Applied a consistent color theme and formatting for clarity and readability

#### Day 3 – Area & Yield Analysis Dashboard (Page 02)
- Designed Page 02: **Paddy Cultivation Area & Yield Analysis**
- Added KPI cards for:
  - Total Area Sown
  - Total Area Harvested
  - Average Yield
- Built a clustered column chart to compare Area Sown vs Area Harvested over time
- Created a stacked column chart showing scheme-wise cultivated area
  (Major, Minor, and Rainfed schemes)
- Added a line chart to visualize average yield trends across years
- Synced slicers (Year, Season, District) with Page 01 for consistent filtering
- Applied consistent formatting and color standards across all visuals

#### Day 4 – Forecast & Performance Analysis Dashboard (Page 03)
- Designed Page 03: **Forecast & Performance Analysis**
- Added KPI cards to summarize:
  - Total Production Gap
  - Average Production Gap Percentage
  - Average Forecast Accuracy
- Built a line chart comparing Actual vs Predicted paddy production over time
- Added a filled map to visualize district-wise production gaps
- Created a bar chart to highlight production gaps by district
- Added a donut chart to classify forecast performance
  (Above Expected, As Expected, Below Expected)
- Included a key insights text box to summarize forecast reliability and gaps
- Synced slicers across all dashboard pages for consistent filtering
- Applied consistent formatting and color standards across the dashboard


