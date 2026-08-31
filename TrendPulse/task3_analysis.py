import pandas as pd          # Used to load and work with the CSV data
import numpy as np           # Used for the required statistical calculations


# Load the cleaned data created by Task 2
input_file = "data/trends_clean.csv"

df = pd.read_csv(input_file)

print(f"Loaded data: {df.shape}")


# Show the first five rows to get a quick look at the data
print("\nFirst 5 rows:")
print(df.head())


# Find the average score and average number of comments
average_score = df["score"].mean()
average_comments = df["num_comments"].mean()

print(f"\nAverage score: {average_score:,.2f}")
print(f"Average comments: {average_comments:,.2f}")


# Use NumPy to calculate the main statistics for story scores
mean_score = np.mean(df["score"])
median_score = np.median(df["score"])
standard_deviation = np.std(df["score"])

maximum_score = np.max(df["score"])
minimum_score = np.min(df["score"])

print("\n--- NumPy Stats ---")
print(f"Mean score: {mean_score:,.2f}")
print(f"Median score: {median_score:,.2f}")
print(f"Std deviation: {standard_deviation:,.2f}")
print(f"Max score: {maximum_score:,}")
print(f"Min score: {minimum_score:,}")


# Count the number of stories in each category
category_counts = df["category"].value_counts()

# Pick the category with the highest number of stories
top_category = category_counts.idxmax()
top_category_count = category_counts.max()

print(
    f"\nMost stories in: "
    f"{top_category} ({top_category_count} stories)"
)


# Find the story that has received the most comments
most_commented = df.loc[
    df["num_comments"].idxmax()
]

print(
    f'Most commented story: '
    f'"{most_commented["title"]}" '
    f'— {most_commented["num_comments"]:,} comments'
)


# Calculate how much discussion a story gets compared with its score
df["engagement"] = (
    df["num_comments"] / (df["score"] + 1)
)


# Mark a story as popular when its score is above the average score
df["is_popular"] = (
    df["score"] > average_score
)


# Save the updated DataFrame for Task 4
output_file = "data/trends_analysed.csv"

df.to_csv(
    output_file,
    index=False
)

print(f"\nSaved to {output_file}")
