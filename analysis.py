import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
print("\n--- TEAM Ratings ---")
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

# Setup the Chart style
plt.figure(figsize=(10, 6)) # Make it big
sns.set_theme(style="darkgrid") # Make it look modern

# Create the Bar Chart (Top 10 Aimers)
top_aimers = data.sort_values(by='HSP', ascending=False).head(10)
sns.barplot(data=top_aimers, x='Player', y='HSP', palette='magma')

# Add Labels (Make it readable)
plt.title('Top 10 VCT Players by Headshot %', fontsize=16)
plt.xlabel('Player Name')
plt.ylabel('Headshot Percentage')
plt.xticks(rotation=45) # Rotate names so they don't overlap

# Show/Save it
plt.tight_layout()
plt.savefig('aim_gods_chart.png') # This saves the image!
plt.show()
