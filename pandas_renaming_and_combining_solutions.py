# Setup
import pandas as pd

# Load the wine reviews dataset
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# 1. Rename region_1 and region_2
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})

# 2. Set the index name to 'wines'
reindexed = reviews.rename_axis('wines')

# 3. Combine gaming and movie products data
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"
combined_products = pd.concat([gaming_products, movie_products])

# 4. Join powerlifting meets and competitors on MeetID
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(
    powerlifting_competitors.set_index("MeetID")
)
