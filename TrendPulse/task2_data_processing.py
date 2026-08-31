import pandas as pd          # Used to read, clean and work with the story data
import glob                 # Used to find all files matching a particular pattern
import os                   # Used for working with files and folders


# Look inside the data folder and find all TrendPulse JSON files
json_files = glob.glob("data/trends_*.json")

# If there are no JSON files, stop the program and show an error
if not json_files:
    raise FileNotFoundError(
        "No TrendPulse JSON file was found in the data folder."
    )

# Sort the files by name and pick the latest one
input_file = sorted(json_files)[-1]

# Read the selected JSON file and put the data into a DataFrame
df = pd.read_json(input_file)

print(f"Loaded {len(df)} stories from {input_file}")


# Remove duplicate stories using the post ID
df = df.drop_duplicates(subset="post_id")

print(f"After removing duplicates: {len(df)}")


# Remove stories where title, score or category is missing
df = df.dropna(subset=["title", "score", "category"])

print(f"After removing missing values: {len(df)}")


# Convert the score column into numbers
df["score"] = pd.to_numeric(
    df["score"], errors="coerce"
)

# Convert the comments column into numbers
df["num_comments"] = pd.to_numeric(
    df["num_comments"], errors="coerce"
)


# Remove rows where the number conversion failed
df = df.dropna(
    subset=["score", "num_comments"]
)

# Change the numeric values into integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# Keep only stories that have at least 2 upvotes
df = df[df["score"] >= 2]

print(f"After removing low scores: {len(df)}")


# Remove extra spaces from the beginning and end of titles
df["title"] = df["title"].str.strip()

# Remove extra spaces from author names
# If an author is missing, use "unknown" instead
df["author"] = df["author"].fillna("unknown").str.strip()


# Save the cleaned data as a CSV file
output_file = "data/trends_clean.csv"

df.to_csv(output_file, index=False)

print(f"Saved {len(df)} rows to {output_file}")


# Show how many stories we have in each category
print("\nStories per category:")

category_counts = df["category"].value_counts()

# Print each category along with its story count
for category, count in category_counts.items():
    print(f"{category:<15} {count}")