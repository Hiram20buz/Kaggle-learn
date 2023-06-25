# Code you have previously used to load data
import pandas as pd

# Path of the file to read
iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)
print(home_data.columns)
y = home_data.SalePrice
# Create the list of features below
feature_names = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF",
                      "FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]

X=home_data[feature_names]
# print description or statistics from X
print(X.describe())

# print the top few lines
print(X.head())

from sklearn.tree import DecisionTreeRegressor
#specify the model.
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X, y)

predictions = iowa_model.predict(X)
print(predictions)
print(iowa_model.predict(X.head()))
