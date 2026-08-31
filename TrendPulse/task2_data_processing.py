import pandas as pd          # Used to load and clean the data
import glob                  # Used to find the JSON file
import os                    # Used for working with folders


# Find the latest TrendPulse JSON file
json_files = glob.glob("data/trends_*.json")

if not json_files:
    raise FileNotFoundError(
        "No TrendPulse JSON file was found in the data folder."
    )

# Pick the latest JSON file
input_file = sorted(json_files)[-1]

# Load the JSON data into a Pandas DataFrame
df = pd.read_json(input_file)

print(f"Loaded {len(df)} stories from {input_file}")


# Remove duplicate stories using their post ID
df = df.drop_duplicates(subset="post_id")

print(f"After removing duplicates: {len(df)}")


# Remove rows if any important field is missing
df = df.dropna(
    subset=["post_id", "title", "score"]
)

print(f"After removing nulls: {len(df)}")


# Make sure score and number of comments are numeric
df["score"] = pd.to_numeric(
    df["score"], errors="coerce"
)

df["num_comments"] = pd.to_numeric(
    df["num_comments"], errors="coerce"
)


# Remove rows where the numeric conversion failed
df = df.dropna(
    subset=["score", "num_comments"]
)


# Convert score and comments to integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# Remove stories with a score below 5
df = df[df["score"] >= 5]

print(f"After removing low scores: {len(df)}")


# Remove extra spaces from story titles
df["title"] = df["title"].str.strip()


# Clean author names and use "unknown" when the author is missing
df["author"] = (
    df["author"]
    .fillna("unknown")
    .str.strip()
)


# Save the cleaned data as a CSV file
output_file = "data/trends_clean.csv"

df.to_csv(
    output_file,
    index=False
)

print(f"Saved {len(df)} rows to {output_file}")


# Show how many stories are present in each category
print("\nStories per category:")

category_counts = df["category"].value_counts()

for category, count in category_counts.items():
    print(f"{category:<15} {count}")
