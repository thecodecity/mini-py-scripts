import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Generate a sample dataset (or replace with a real CSV file)
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Sales": [200, 220, 250, 280, 300, 320],
    "Profit": [50, 70, 80, 90, 100, 110],
    "Customer_Count": [30, 35, 40, 50, 55, 60],
}
df = pd.DataFrame(data)

# **1. Line Plot of Sales Trend**
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Sales"], marker="o", linestyle="-", color="b", label="Sales")
plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales", fontsize=12)
plt.legend()
plt.grid(True)
plt.savefig("sales_trend.png")  # Save as an image
plt.show()
plt.close()
# **2. Bar Plot: Sales vs. Profit**
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x="Month", y="Sales", data=df, label="Sales", color="b", alpha=0.7)
sns.barplot(x="Month", y="Profit", data=df, label="Profit", color="g", alpha=0.7)
plt.title("Sales vs Profit by Month", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.legend(title="Metric")
plt.savefig("sales_vs_profit.png")
plt.show()

# **3. Scatter Plot: Customer Count vs Profit**
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Customer_Count", y="Profit", hue="Month", palette="viridis", data=df, s=100)
plt.title("Customer Count vs Profit", fontsize=16)
plt.xlabel("Customer Count", fontsize=12)
plt.ylabel("Profit", fontsize=12)
plt.savefig("customer_vs_profit.png")
plt.show()

# **4. Interactive Dashboard Using Plotly**
fig = px.line(
    df,
    x="Month",
    y=["Sales", "Profit"],
    title="Interactive Sales and Profit Trends",
    labels={"value": "Values", "variable": "Metric"},
    markers=True,
)
fig.write_html("interactive_dashboard.html")  # Save as an HTML file
fig.show()
