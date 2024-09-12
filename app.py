# Install streamlit
#!pip install streamlit

# Import libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import pandas as pd

# Read data
df = pd.read_csv('E:\Streamlit App\defects_data.csv')

# Convert to date
df.defect_date=pd.to_datetime(df.defect_date)
# Add a column with defect month, eg: '2024-06'

df=df.assign(defect_month=df.defect_date.dt.strftime('%Y-%m'))

# Count the number of product_ids with defects on a monthly basis

monthly_defects=df.groupby('defect_month',as_index=False).product_id.count()


# Configure page to wide layout
st.set_page_config(layout="wide")

# Add app title 
st.title("Defective Products Insights")

# Show data
st.dataframe(
    data=df,
    hide_index=True,
    use_container_width=True,
)

# Add a subheader
st.subheader("Monthly Product Defect Trends")
st.write(" ")

# Add left and right columns
left,right=st.columns(2,gap="small")

# Create line chart for monthly trends in left column
left.line_chart(
    data=monthly_defects,
    x="defect_month",
    y="product_id",
    color="#FF3389",
    x_label="",
    y_label="Defective Products",
    use_container_width=True,
)

# Show summary data on the right side
right.dataframe(
    monthly_defects.style.format(thousands=",",precision=2).highlight_max(subset=["product_id"]),
    use_container_width=True,
)

# Group data by product_id and calculate the total repair cost
product_stats=df.groupby('product_id',as_index=False).agg({'defect_id':'count','repair_cost':'sum'}).sort_values(by='repair_cost',ascending=False)
top_repairs=product_stats[:10]

# Create chart to show the top 10 products by repair cost
fig,ax=plt.subplots(figsize=(8,6))
g=sns.barplot(data=top_repairs,y='product_id',x='repair_cost',
              order=top_repairs.product_id,palette='Set1',
              errorbar=None,orient='h')
# Specify formatting and labels
_=ax.get_xaxis().set_major_formatter(ticker.FuncFormatter(lambda x,p:format(int(x),',')))
_=ax.set_xlabel("Total Repair Cost")
_=ax.set_ylabel("Product Id")

# Add a subheader and divider for a new section
# Add a subheader and divider for a new section
st.subheader(
    "Top 10 Product Repair Cost",
    divider="blue",
)
# Create 2 new columns
left_col, right_col = st.columns(2, gap="small")

# Plot figure on the left
left_col.pyplot(fig=fig, use_container_width=True)

# Show dataframe on the right
right_col.dataframe(
    top_repairs.style.format(thousands=",", precision=2).highlight_max(
        subset=["repair_cost"]
    ),
    use_container_width=True,
    hide_index=True,
)

# Seaborn catplot for average repair cost by inspection method and month
g = sns.catplot(
    data=df, x='defect_month', y='repair_cost', col='inspection_method',
    col_order=['Manual Testing', 'Visual Inspection', 'Automated Testing'],
    kind='point', errorbar=None, color='blue', aspect=.95
)

# Add new section for average repair cost plot
st.subheader("Average Repair Cost by Inspection Method and Month")

# Create three columns with smaller left and right and a larger center
col1, col2, col3 = st.columns([0.5, 5, 0.5])  # Narrow left and right columns

# Display the Seaborn plot in one of the columns
with col2:
    st.pyplot(g.fig)