# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for a professional look
sns.set_style("whitegrid")
sns.set_context("talk")  # Presentation-ready text sizes

# Generate realistic synthetic data
np.random.seed(42)  # For reproducibility

# Define customer segments
segments = ["Bronze", "Silver", "Gold", "Platinum"]

# Generate purchase amounts (in dollars) per segment
data = {
    "Customer Segment": np.repeat(segments, 50),  # 50 customers per segment
    "Purchase Amount": np.concatenate([
        np.random.normal(50, 15, 50),     # Bronze
        np.random.normal(120, 30, 50),    # Silver
        np.random.normal(250, 50, 50),    # Gold
        np.random.normal(500, 100, 50)    # Platinum
    ])
}

df = pd.DataFrame(data)

# Create the boxplot
plt.figure(figsize=(8, 8))  # 512x512 pixels
box = sns.boxplot(
    x="Customer Segment",
    y="Purchase Amount",
    data=df,
    palette="Set2",
    showfliers=True
)

# Customize titles and labels
plt.title("Customer Purchase Amount Distribution by Segment", fontsize=16, weight='bold')
plt.xlabel("Customer Segment", fontsize=14)
plt.ylabel("Purchase Amount ($)", fontsize=14)

# Save the chart
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
