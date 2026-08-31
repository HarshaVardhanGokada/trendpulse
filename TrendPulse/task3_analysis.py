import pandas as pd          # Used to read and work with the CSV data
import numpy as np           # Used for statistical calculations


# This is the cleaned data created by Task 2
input_file = "data/trends_clean.csv"

# Read the cleaned CSV file into a DataFrame
df = pd.read_csv(input_file)

print(f"Loaded data: ({len(df)}, {len(df.columns)})")


# Show the first 5 stories so we can quickly check the data
print("\nFirst 5 rows:")
print(df.head())


# Find the average score and average number of comments
average_score = df["score"].mean()
average_comments = df["num_comments"].mean()

print(f"\nAverage score: {average_score:,.2f}")
print(f"Average comments: {average_comments:,.2f}")


# Use NumPy to calculate some important statistics
mean_score = np.mean(df["score"])
median_score = np.median(df["score"])
standard_deviation = np.std(df["score"])

# Find the highest and lowest story scores
maximum_score = df["score"].max()
minimum_score = df["score"].min()

print(f"\nMean score: {mean_score:,.2f}")
print(f"Median score: {median_score:,.2f}")
print(f"Standard deviation: {standard_deviation:,.2f}")
print(f"Maximum score: {maximum_score:,}")
print(f"Minimum score: {minimum_score:,}")


# Count how many stories are present in each category
category_counts = df["category"].value_counts()

# Find the category that has the most stories
top_category = category_counts.idxmax()
top_category_count = category_counts.max()

print(
    f"\nMost stories in: "
    f"{top_category} ({top_category_count} stories)"
)


# Find the story that received the most comments
most_commented = df.loc[
    df["num_comments"].idxmax()
]

print(
    f'Most commented story: '
    f'"{most_commented["title"]}" '
    f'— {most_commented["num_comments"]:,} comments'
)


# Save the analysed data so Task 4 can use it for visualization
output_file = "data/trends_analysed.csv"

df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")