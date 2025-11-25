import pandas as pd

# Load the csv data
data = pd.read_csv('overall_player_stats.csv')

# Fix the Headshot % column: remove the '%' sign and make it a number
data['HSP'] = data['HSP'].str.replace('%', '').astype(float)

# --- 1. Top Players by Rating ---
print("--- TOP 5 PLAYERS (RATING) ---")
print(data[['Player', 'Team', 'Rating', 'HSP']].head(5))

# --- 2. Best Aimers ---
print("\n--- AIM GODS (HIGHEST HEADSHOT %) ---")
# Sort by HSP to find who has the crispest aim
aimers = data.sort_values(by='HSP', ascending=False)
print(aimers[['Player', 'Team', 'HSP']].head(5))

# --- 3. Best Teams ---
print("\n--- TEAM POWER RANKINGS ---")
# Group by Team to see who has the best average stats
team_stats = data.groupby('Team')[['Rating', 'HSP']].mean()
# Sort them so the best team is at the top
team_stats = team_stats.sort_values(by='Rating', ascending=False)
print(team_stats.head(5))

# --- 4. Best Entry Fraggers ---
print("\n--- ENTRY GODS (FIRST BLOOD SUCCESS) ---")
# Logic: First Kills / (First Kills + First Deaths)
data['Entry_Success'] = data['FK'] / (data['FK'] + data['FD'])

# Sort to find the best entry players
entry_gods = data.sort_values(by='Entry_Success', ascending=False)
print(entry_gods[['Player', 'Team', 'Entry_Success']].head(5))