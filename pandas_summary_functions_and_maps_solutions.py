import pandas as pd

pd.set_option("display.max_rows", 5)

# Load dataset
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Median of points column
median_points = reviews['points'].median()

# Unique countries in the dataset
countries = reviews['country'].unique()

# Number of reviews per country
reviews_per_country = reviews['country'].value_counts()

# Centered price column
mean_price = reviews['price'].mean()
centered_price = reviews['price'] - mean_price

# Best bargain wine (highest points-to-price ratio)
reviews['points_to_price'] = reviews['points'] / reviews['price']
best_bargain_index = reviews['points_to_price'].idxmax()
bargain_wine = reviews.loc[best_bargain_index, 'title']

# Count how many times 'tropical' and 'fruity' appear in descriptions
n_trop = reviews['description'].map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews['description'].map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

# Star ratings logic
def get_star_rating(row):
    if row['country'] == 'Canada':
        return 3
    elif row['points'] >= 95:
        return 3
    elif row['points'] >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(get_star_rating, axis=1)
