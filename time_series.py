import pandas as pd
import matplotlib.pyplot as plt

# Read in the time series data
data = pd.read_csv('Microsoft_stock.csv')

print(data.info())

print(data.shape)

print(data.describe())

print(data.corr())

data.isnull().sum()  # cheaking if any colomns is left empty or not.

print(data.cov())

# Convert the 'date' column to a datetime object
data['Date'] = pd.to_datetime(data['Date'])

# Set the 'date' column as the index of the DataFrame
data.set_index('Date', inplace=True)

# Print the first few rows of the DataFrame
print(data.head())

# Plot the time series data
data.plot()

# Show the plot
plt.show()

