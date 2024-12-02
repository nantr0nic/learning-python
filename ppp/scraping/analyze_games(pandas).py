# This is something the AI suggested to try/check out with Pandas

import pandas as pd
import json

# Read your JSON file
with open('steam_new_releases.json', 'r') as f:
    data = json.load(f)

# Create DataFrame from games data
df = pd.DataFrame(data['games'])

# Now you can do interesting analyses:
# Average price of games
print(f"Average price: {df['price'].str.replace('$', '').astype(float).mean():.2f}")

# Count of games by platform
platform_counts = df['platforms'].explode().value_counts()
print("\nGames per platform:")
print(platform_counts)

# Most common tags
all_tags = df['tags'].explode()
print("\nMost common tags:")
print(all_tags.value_counts().head())