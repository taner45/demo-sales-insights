import pandas as pd

# Assuming data is loaded from 'data/modified_supermarkt_sales_plus.csv'
data = pd.read_csv("data/modified_supermarkt_sales_plus.csv")

data["Date"] = pd.to_datetime(data["Date"])
data["Month_Year"] = data["Date"].dt.to_period("M").dt.to_timestamp()
