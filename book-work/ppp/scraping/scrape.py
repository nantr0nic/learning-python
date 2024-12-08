import requests
import lxml.html
import json
from datetime import datetime
import pandas as pd

# Set up the web scraping crap
html = requests.get("https://store.steampowered.com/explore/new/")
doc = lxml.html.fromstring(html.content)

# Define the table/dropdown/element area we want to be pulling the other xpath elements from
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
# Define/find the titles and prices
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

# Find and put into a list the genre tags of each game
tags = [tag.text_content() for tag in new_releases.xpath('//div[@class="tab_item_top_tags"]')]
# list comprehension ^^^^
# split list with commas vvv
tags = [tag.split(", ") for tag in tags]
# Platforms are not labeled, they're spans in the bottom div vvv
platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    # Loop through / find each element in platforms_div
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    # They're not titled so splitting off the last part (e.g. win, mac, linux, etc.)
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    # Remove separator for VR stuff
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)

output = []

for info in zip(titles, prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)

# Add Timestamp 
final_output = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "games": output
}

json_output = json.dumps(final_output, indent=2)

with open("steam_new_releases.json", "w", encoding="utf-8") as file:
    json.dump(final_output, file, indent=2)

with open("steam_new_releases.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Create DataFrame from the games data
df = pd.DataFrame(data['games'])

# Format the tags and platforms columns to be more readable
df['tags'] = df['tags'].apply(lambda x: ', '.join(x))
df['platforms'] = df['platforms'].apply(lambda x: ', '.join(x))

# Set display options for better viewing
pd.set_option('display.max_rows', None)        # Show all rows
pd.set_option('display.max_columns', None)     # Show all columns
pd.set_option('display.width', None)           # Auto-detect display width
pd.set_option('display.max_colwidth', None)    # Show full content of each cell

# Print the timestamp and the data
print(f"\nData collected at: {data['timestamp']}\n")
print(df)