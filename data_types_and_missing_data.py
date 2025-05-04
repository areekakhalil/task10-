# data_types_and_missing_data.py

# Step 1: Load data and setup
import pandas as pd

# Load the dataset
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Load check tools from learntools
from learntools.core import binder
binder.bind(globals())

from learntools.pandas.data_types_and_missing_data import *

print("Setup complete.")

# ----------------------------------------
# Exercise 1: Get data type of 'points' column
dtype = reviews['points'].dtype
q1.check()
print("Data type of 'points' column:", dtype)

# ----------------------------------------
# Exercise 2: Convert 'points' column to strings
point_strings = reviews['points'].astype(str)
q2.check()
print("Converted 'points' column to strings (first 5):")
print(point_strings.head())

# ----------------------------------------
# Exercise 3: Count missing values in 'price' column
n_missing_prices = reviews['price'].isnull().sum()
q3.check()
print("Number of missing prices:", n_missing_prices)

# ----------------------------------------
# Exercise 4: Fill missing 'region_1' with 'Unknown' and count occurrences
reviews['region_1'] = reviews['region_1'].fillna('Unknown')
reviews_per_region = reviews['region_1'].value_counts().sort_values(ascending=False)
q4.check()
print("Most common regions (top 5):")
print(reviews_per_region.head())
