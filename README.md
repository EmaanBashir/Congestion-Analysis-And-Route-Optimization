# Congestion Analysis and Route Optimization for Buses

## Project Overview
This project aims to analyze traffic congestion patterns on Nottingham City Transport (NCT) bus routes and optimize bus routes to improve efficiency. Using real-time bus location data from the Bus Open Data Service (BODS), various congestion analysis techniques and optimization algorithms were applied to identify and propose better routes.

<p align="center">
  <img src="https://github.com/user-attachments/assets/01082809-49b1-4aa9-80d4-9b9585ec7f06" height="200">
  <img src="https://github.com/user-attachments/assets/85e350f2-f228-4200-8c38-0e7328a45df8" height="200">
</p>

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Results](#results)
- [Requirements](#requirements)
- [How to Run the Code](#how-to-run-the-code)
- [Future Work](#future-work)
- [References](#references)
- [Presentation](#presentation)

## Technologies Used
- Python
- Pandas, NumPy (Data Processing)
- Matplotlib, Seaborn (Data Visualization)
- Scikit-learn (Machine Learning for Clustering)
- NetworkX (Graph-Based Route Optimization)
- HDF5 (Data Storage)

## Data Sources
- **Bus Location Data**: Real-time bus location data from the Bus Open Data Service API, fetched every 15 seconds.
- **Bus Timetable Data**: TransXChange (TXC) formatted XML data providing bus schedules and planned routes.

## Methodology
![image](https://github.com/user-attachments/assets/d542b3b0-de5d-47a2-b719-74166ba4936a)

### Data Collection and Preprocessing
- **Parsing XML Data**: Extracted real-time bus location and timetable data.
- **Data Cleaning**: Removed duplicates, handled missing values, and converted data types.
- **Feature Engineering**: Calculated travel times, extracted congestion patterns, and mapped location data to schedules.

### Identification of Congested Routes
- **Exploratory Data Analysis (EDA)**: Histograms and box plots to visualize congestion patterns.

  ![image](https://github.com/user-attachments/assets/66440b6f-130c-44f9-85c7-358d4c461591)

- **Clustering Techniques**: Used k-Means and DBSCAN to classify congestion levels into Low, Medium, and High categories.

![image](https://github.com/user-attachments/assets/d902448d-4647-40ef-86ac-ba7ba1cf0c73)

### Congestion Analysis
- **Distribution of Congestion Levels**:
  
  ![image](https://github.com/user-attachments/assets/5ed1692b-c0ca-4daa-8c14-2c5d3f0a62d3)
  ![image](https://github.com/user-attachments/assets/e895e46a-5ccd-481e-b20f-4f844ecd39d4)

-  **Visualization of Congestion Levels on the Map**:
  
  ![image](https://github.com/user-attachments/assets/c824d972-02c0-4b6d-b157-a723534307f9)

-  **Analysis of Congestion by Route Section**:
  
  ![image](https://github.com/user-attachments/assets/8d2f5980-6518-498d-ab58-1582abc4f208)
  ![image](https://github.com/user-attachments/assets/be13367d-8a9e-41be-a1b8-812c9e8e1dc9)

-  **Congestion Analysis by Day of the Week**:
  
  ![image](https://github.com/user-attachments/assets/a790dc2f-d014-4dab-b1a6-4b669723c89e)

-  **Congestion Analysis by Time Interval**:
  
  ![image](https://github.com/user-attachments/assets/fd3abdd2-fb29-4b03-b40d-50d3e531660f)

### Route Optimization
- **Graph Representation**: Represented bus stops and routes as a directed graph.

  ![image](https://github.com/user-attachments/assets/c2971a47-ccd9-471b-8ad2-101165d3ddc8)

- **Dijkstra’s Algorithm**: Used for finding the shortest path (least travel time) between two stops.
- **Alternative Routes**: Suggested for high-congestion areas with over 70% congestion.

![image](https://github.com/user-attachments/assets/76d117cf-84de-4861-8f77-0ba8b5ed6013)
![image](https://github.com/user-attachments/assets/de323ea0-b3b7-4c8c-a75f-9e46251d38b9)

## Results
- Identified peak congestion times (8:00 - 18:00) and high-traffic routes.
- Proposed alternative routes for high-congestion areas, reducing average travel time by 12.89%.
- Statistically significant improvements confirmed via paired t-tests.

  ![image](https://github.com/user-attachments/assets/4f67d941-5c91-454b-835e-4eece59f7adb)

## Requirements
To run this project, you need the following dependencies:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn folium networkx lxml
```

## How to Run the Code
1. Clone the repository:
```bash
git clone https://github.com/EmaanBashir/Congestion-Analysis-And-Route-Optimization.git
cd Congestion-Analysis-And-Route-Optimization/Code
```
2. Run the data collection script to fetch real-time bus location data:
```bash
python Location_data_collection_script.py
```
3. Preprocess the data using:
```bash
jupyter notebook Location_Data_Preprocessing.ipynb
```
```bash
jupyter notebook Timetable_Data_Preprocessing.ipynb
```
4. Run the congestion analysis and optimization:
```bash
jupyter notebook Congestion_Analysis_and_Route_Optimization.ipynb
```

## Future Work
- Integrate real-time traffic data for dynamic route adjustments.
- Consider weather conditions and roadworks in congestion analysis.
- Incorporate passenger boarding patterns for better optimization.
- Explore adding new bus stops for further efficiency improvements.

## References
- Almeida, A., et al. (2023) ‘Exploring bus tracking data to characterize urban traffic congestion’, *Journal of Urban Mobility.*
- Ma, J., et al. (2019) ‘Bus travel time prediction with real-time traffic information’, *Transportation Research Part C.*
- Huang, K., et al. (2020) ‘Customized Bus Route Optimization with Real-Time Data’, *Journal of Advanced Transportation.*

## Presentation
[Click here to view the presentation](https://www.canva.com/design/DAGQPEFjIrw/f43lnIKUbaRF3DeZ6CKLlA/edit?utm_content=DAGQPEFjIrw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---
For more details view the Dissertation.pdf present in the repository
