import pandas as pd
import os
import matplotlib.pyplot as plt

# Some comments here
dates = pd.date_range("20130101", periods=6)

print("test")

# Create sample data
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Sales': [100, 120, 140, 160, 180, 200, 220, 240, 260, 280]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame:")
print(df)
print()

# Plot the data using Matplotlib
plt.plot(df['Year'], df['Sales'], marker='o')
plt.title('Yearly Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
