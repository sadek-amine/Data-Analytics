import pandas as pd
import matplotlib.pyplot as plt

position = pd.read_csv("baseball_positions.csv")



# Create DataFrame
df = pd.DataFrame(data, columns=["Name", "Team", "Position"])

# Split multiple positions
df["Position"] = df["Position"].str.split("/")

# Expand rows (important step)
df = df.explode("Position")

# Count players per position
position_counts = df["Position"].value_counts()

# Convert to table
result = position_counts.reset_index()
result.columns = ["Position", "Player Count"]

print(result)