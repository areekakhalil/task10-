# grouping_and_sorting.py

# Step 1: Load data and setup
import pandas as pd

# Load the dataset
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Load check tools from learntools
from learntools.core import binder
binder.bind(globals())

from learntools.pandas.grouping_and_sorting import *

print("Setup complete.")

# ----------------------------------------
# Exercise 1: Count reviews per reviewer (twitter handle)
reviews_written = reviews.groupby('taster_twitter_handle').size()
q1.check()
print("Number of reviews per Twitter handle:")
print(reviews_written)

# ----------------------------------------
# Exercise 2: Best rating per price
best_rating_per_price = reviews.groupby('price')['points'].max()
best_rating_per_price = best_rating_per_price.sort_index()
q2.check()
print("Best wine rating per price (top 5):")
print(best_rating_per_price.head())

# ----------------------------------------
# Exercise 3: Min and max price for each variety
price_extremes = reviews.groupby('variety')['price'].agg(['min', 'max'])
q3.check()
print("Min and max price per variety (top 5):")
print(price_extremes.head())

# ----------------------------------------
# Exercise 4: Sort varieties by min and max price (descending)
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=[False, False])
q4.check()
print("Most expensive varieties sorted (top 5):")
print(sorted_varieties.head())

# ----------------------------------------
# Exercise 5: Average score per reviewer (by name)
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()
q5.check()
print("Average points per reviewer:")
print(reviewer_mean_ratings)

# Optional: Summary stats to analyze variation
print("\nReviewer mean ratings summary:")
print(reviewer_mean_ratings.describe())

# ----------------------------------------
# Exercise 6: Count of {country, variety} wine combinations
country_variety_counts = reviews.groupby(['country', 'variety']).size()
country_variety_counts = country_variety_counts.sort_values(ascending=False)
q6.check()
print("Most common country-variety combinations (top 5):")
print(country_variety_counts.head())
