# Step 0: Import libraries and load dataset
import pandas as pd

# Load the dataset
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# Step 1: Select the 'description' column
desc = reviews['description']

# Step 2: Select the first value in the 'description' column
first_description = reviews['description'].iloc[0]

# Step 3: Select the first row of data
first_row = reviews.iloc[0]

# Step 4: First 10 descriptions
first_descriptions = reviews['description'].head(10)

# Step 5: Select specific records by index
sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]

# Step 6: Select specific columns for specific rows
data = {
    'country': ['Italy', 'Portugal', 'US', 'US'],
    'province': ['Sicily & Sardinia', 'Douro', 'California', 'New York'],
    'region_1': ['Etna', None, 'Napa Valley', 'Finger Lakes'],
    'region_2': [None, None, 'Napa', 'Finger Lakes']
}
df_step6 = pd.DataFrame(data, index=[0, 1, 10, 100])

# Step 7: First 100 records with 'country' and 'variety'
cols = ['country', 'variety']
df_step7 = reviews.loc[:99, cols]

# Step 8: Create a DataFrame for Italian wines
italian_wines = reviews[reviews['country'] == 'Italy']

# Step 9: Reviews with 95+ points from Australia or New Zealand
top_oceania_wines = reviews[
    (reviews['country'].isin(['Australia', 'New Zealand'])) & (reviews['points'] >= 95)
]
