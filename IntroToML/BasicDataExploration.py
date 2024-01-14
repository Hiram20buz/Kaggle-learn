import pandas as pd


# Define the URL
melbourne_url = 'train.csv'

# Read the data from the URL and store it in a DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_url)

# Print a summary of the data in Melbourne data
print(melbourne_data.describe())
