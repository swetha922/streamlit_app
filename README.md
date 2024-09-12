# Defective Products Insights Dashboard with Streamlit
This project is an interactive dashboard built using Streamlit to analyze and visualize trends in product defects and repair costs. The dashboard provides insights into product performance, defect frequency, and repair costs, helping to identify top defective products and their associated inspection methods.

# Project Features:
Monthly Defect Trends: Visualize the number of defective products reported each month using an interactive line chart.
Top 10 Products by Repair Cost: A bar chart showcasing the products with the highest repair costs to prioritize maintenance efforts.
Inspection Methods Comparison: Using Seaborn’s catplot, the dashboard compares repair costs across different inspection methods (Manual Testing, Visual Inspection, and Automated Testing).

# Technologies Used:
Streamlit: For creating an interactive web app.
Pandas: To process and manipulate the defect dataset.
Seaborn & Matplotlib: For generating insightful visualizations.
Python: Core programming language for data analysis and visualization.
Dataset: The dataset used is taken from Kaggle and includes product defect information such as product IDs, defect dates, inspection methods, and repair costs.

# How to Run:
streamlit run app.py
http://localhost:8501/

This project aims to help businesses understand and monitor product defects over time, enabling more effective product maintenance and quality control strategies.

