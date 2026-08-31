import os                         # Used to create the output folder
import pandas as pd               # Used to read and work with the CSV data
import matplotlib.pyplot as plt   # Used to create the charts


# Load the analysed data created by Task 3
input_file = "data/trends_analysed.csv"

df = pd.read_csv(input_file)


# Create the outputs folder if it is not already there
os.makedirs("outputs", exist_ok=True)


# --------------------------------------------------
# Chart 1: Top 10 stories by score
# --------------------------------------------------

# Sort stories from highest score to lowest
# and keep only the top 10
top_stories = (
    df.sort_values("score", ascending=False)
    .head(10)
    .copy()
)


# Long titles can make the chart difficult to read,
# so this function shortens them
def shorten_title(title):

    if len(title) > 50:
        return title[:50] + "..."

    return title


# Create a shorter title just for displaying in the chart
top_stories["short_title"] = (
    top_stories["title"].apply(shorten_title)
)


# Set the size of the first chart
plt.figure(figsize=(10, 6))


# Create a horizontal bar chart
plt.barh(
    top_stories["short_title"],
    top_stories["score"]
)


# Add labels and a title to make the chart easy to understand
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")


# Put the highest-scoring story at the top
plt.gca().invert_yaxis()

plt.tight_layout()


# Save the first chart as an image
plt.savefig("outputs/chart1_top_stories.png")

# Close the chart after saving it
plt.close()


# --------------------------------------------------
# Chart 2: Number of stories in each category
# --------------------------------------------------

# Count how many stories belong to each category
category_counts = df["category"].value_counts()


# Create the second chart
plt.figure(figsize=(10, 6))


# Draw a bar for each category
plt.bar(
    category_counts.index,
    category_counts.values
)


# Add labels and a title
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")


# Rotate the category names slightly so they are easier to read
plt.xticks(rotation=30)

plt.tight_layout()


# Save the category chart
plt.savefig("outputs/chart2_categories.png")

plt.close()


# --------------------------------------------------
# Chart 3: Score versus number of comments
# --------------------------------------------------

# We use 100 points as the limit for calling a story popular
popular_limit = 100


# Separate stories into popular and not-popular groups
popular = df[df["score"] >= popular_limit]
not_popular = df[df["score"] < popular_limit]


# Create the scatter plot
plt.figure(figsize=(10, 6))


# Plot popular stories
plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.7
)


# Plot stories below the popularity limit
plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    alpha=0.7
)


# Add labels and a title
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")

# Show which points are popular and which are not
plt.legend()

plt.tight_layout()


# Save the scatter plot
plt.savefig("outputs/chart3_scatter.png")

plt.close()


# Tell us that all three charts were created
print("Charts created successfully.")

print("Saved:")
print("outputs/chart1_top_stories.png")
print("outputs/chart2_categories.png")
print("outputs/chart3_scatter.png")