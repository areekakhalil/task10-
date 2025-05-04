# data_analytics_intro.py

# Step 1: Import libraries
import pandas as pd
pd.set_option('display.max_rows', 5)

from learntools.core import binder
binder.bind(globals())

from learntools.pandas.creating_reading_and_writing import *

print("Setup complete.")

# Step 2: Exercise 1 - Create a simple DataFrame
fruits = pd.DataFrame({
    'Apples': [30],
    'Bananas': [21]
})

# Check answer
q1.check()
print(fruits)

# Step 3: Exercise 2 - Create a DataFrame with index labels
fruit_sales = pd.DataFrame({
    'Apples': [35, 41],
    'Bananas': [21, 34]
}, index=["2017 Sales", "2018 Sales"])

# Check answer
q2.check()
print(fruit_sales)

# Step 4: Exercise 3 - Create a Series with a name and custom index
quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
ingredients = pd.Series(quantities, index=items, name='Dinner')

# Check answer
q3.check()
print(ingredients)

# Step 5: Exercise 4 - Read CSV file into DataFrame
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# Check answer
q4.check()
print(reviews.head())

# Step 6: Exercise 5 - Save a DataFrame to a CSV file
animals = pd.DataFrame({
    'Cows': [12, 20],
    'Goats': [22, 19]
}, index=['Year 1', 'Year 2'])

print(animals)

# Save to disk
animals.to_csv('cows_and_goats.csv')

# Check answer
q5.check()
