import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('Top 50 US Tech Companies 2022 - 2023.csv')

# Calculate the total number of companies in the dataset
total_companies = len(df)
print("Total number of companies in the dataset:", total_companies)

# Calculate the number of companies by industry
sector_count = df.groupby(['Sector']).size().reset_index(name='Count')
print(sector_count)

# Calculate the average revenue by industry
industry_revenue = df.groupby(['Sector'])['Annual Revenue 2022-2023 (USD in Billions)'].mean().reset_index(name='Average Revenue')
print(industry_revenue)

# Calculate the correlation between revenue and market cap
revenue_marketcap_corr = df['Annual Revenue 2022-2023 (USD in Billions)'].corr(df['Market Cap (USD in Trillions)'])
print("Correlation between Revenue and Market Cap:", revenue_marketcap_corr)

# Create a histogram of founding years
plt.hist(df['Founding Year'], bins=range(1950, 2025, 5))
plt.title("Histogram of Founding Years")
plt.xlabel("Founding Year")
plt.ylabel("Count")
plt.show()

# Create a scatter plot of revenue vs market cap
plt.scatter(df['Annual Revenue 2022-2023 (USD in Billions)'], df['Market Cap (USD in Trillions)'])
plt.title("Revenue vs Market Cap")
plt.xlabel("Annual Revenue (in Billions USD)")
plt.ylabel("Market Cap (in Trillions USD)")
plt.show()

# Create a pie chart of the number of companies by industry
plt.pie(sector_count['Count'], labels=sector_count['Sector'], autopct='%1.1f%%')
plt.title("Number of Companies by Industry")
plt.show()
