import pandas as pd

melbourne_file_path = 'train.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]
X.describe()
X.head()
