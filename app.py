import streamlit as st
import pandas as pd

st.set_page_config(page_title="Qahwa Corner", page_icon="☕", layout="wide")

st.title("☕ Qahwa Corner Dashboard")
st.write("Sales Report | January - June 2026")

# Read sales data
df = pd.read_csv("cafe_sales.csv")

# Choose branch
branch = st.selectbox("Choose a Branch:", df["branch"].unique())

# Filter sales by branch
sales = df[df["branch"] == branch]

# Calculate total revenue
revenue = sales["total_sar"].sum()

st.metric("Total Sales (SAR)", f"{revenue:,.0f} SAR")

# Calculate revenue for each product
products = sales.groupby("product")["total_sar"].sum()

# Display chart
st.subheader("Sales by Product")
st.bar_chart(products)
