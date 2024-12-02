import json

# Read the JSON file
with open("steam_new_releases.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    games = data['games'] # Get games list from data

# 1. Find all games under a certain price
def find_cheap_games(max_price):
    cheap_games = []
    for game in games: # Access games list in JSON
        price = game['price']
        if price == "Free To Play":
            cheap_games.append(game) # Include free games
        else:
            try:
                price_value = float(price.replace("$", "").strip()) # remove dollar sign
                if price_value < max_price:
                    cheap_games.append(game)
            except ValueError:
                # Skip the shit that breaks my shit muthafucka
                continue
        return cheap_games


# 2. Find games by platform
def find_games_by_platform(platform):
    return [game for game in games if platform in game['platforms']]

# 3. Find games by tag
def find_games_by_tag(tag):
    return [game for game in games 
            if tag.lower() in [t.lower() for t in game['tags']]]

# Print some example analyses
print("\nGames under $20:")
cheap_games = find_cheap_games(20)
for game in cheap_games:
    print(f"{game['title']} - {game['price']}")

print("\nWindows games:")
windows_games = find_games_by_platform('win')
for game in windows_games:
    print(game['title'])

print("\nRPG games:")
rpg_games = find_games_by_tag('RPG')
for game in rpg_games:
    print(f"{game['title']} - Tags: {', '.join(game['tags'])}")