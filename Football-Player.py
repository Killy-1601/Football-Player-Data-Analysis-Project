import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = "player_profiles.csv"   # change path if needed
df = pd.read_csv(file_path)

# ===============================
# 1. Top 10 countries with most players
# ===============================
top_countries = df['country_of_birth'].value_counts().head(10)

plt.figure(figsize=(10,6))
top_countries.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Top 10 Countries with Most Players")
plt.xlabel("Country")
plt.ylabel("Number of Players")
plt.xticks(rotation=45, ha="right")
plt.show()

# ===============================
# 2. Distribution of player positions
# ===============================
positions = df['main_position'].value_counts().head(10)

plt.figure(figsize=(10,6))
positions.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Distribution of Player Positions (Top 10)")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.xticks(rotation=45, ha="right")
plt.show()

# ===============================
# 3. Left-footed vs Right-footed players
# ===============================
footed = df['foot'].value_counts()

plt.figure(figsize=(6,6))
footed.plot(kind="pie", autopct="%1.1f%%", colors=["lightblue","lightgreen","lightcoral"])
plt.title("Foot Preference of Players")
plt.ylabel("")
plt.show()

# ===============================
# 4. Height distribution
# ===============================
plt.figure(figsize=(10,6))
df['height'].dropna().plot(kind="hist", bins=30, color="purple", edgecolor="black")
plt.title("Distribution of Player Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Number of Players")
plt.show()

# ===============================
# 5. Average height by main position
# ===============================
avg_height = df.groupby("main_position")["height"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
avg_height.plot(kind="bar", color="green", edgecolor="black")
plt.title("Average Height by Player Position (Top 10)")
plt.xlabel("Position")
plt.ylabel("Average Height (cm)")
plt.xticks(rotation=45, ha="right")
plt.show()
