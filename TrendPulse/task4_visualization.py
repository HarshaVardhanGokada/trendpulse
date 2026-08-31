import os
import pandas as pd
import matplotlib.pyplot as plt


# Load the analysed data created by Task 3
input_file = "data/trends_analysed.csv"
df = pd.read_csv(input_file)

# Create the outputs folder if it is not already there
os.makedirs("outputs", exist_ok=True)


# Shorten long story titles so they fit nicely on the chart
def shorten_title(title):
    if len(title) > 50:
        return title[:50] + "..."
    return title


# --------------------------------------------------
# Chart 1: Top 10 stories by score
# --------------------------------------------------

top_stories = (
    df.sort_values("score", ascending=False)
    .head(10)
    .copy()
)

top_stories["short_title"] = (
    top_stories["title"].apply(shorten_title)
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_stories["short_title"],
    top_stories["score"]
)

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

# Put the highest-scoring story at the top
plt.gca().invert_yaxis()

plt.tight_layout()

# Save the chart before closing the figure
plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# --------------------------------------------------
# Chart 2: Number of stories in each category
# --------------------------------------------------

category_counts = df["category"].value_counts()

plt.figure(figsize=(10, 6))

# Give every category bar its own colour
plt.bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("outputs/chart2_categories.png")
plt.close()


# --------------------------------------------------
# Chart 3: Score versus number of comments
# --------------------------------------------------

# Separate stories using the is_popular column from Task 3
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(10, 6))

plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.7
)

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    alpha=0.7
)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.tight_layout()

plt.savefig("outputs/chart3_scatter.png")
plt.close()


# --------------------------------------------------
# Bonus: Combine all three charts into one dashboard
# --------------------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Dashboard Chart 1
axes[0].barh(
    top_stories["short_title"],
    top_stories["score"]
)

axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story Title")
axes[0].set_title("Top 10 Stories by Score")
axes[0].invert_yaxis()


# Dashboard Chart 2
axes[1].bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

axes[1].set_xlabel("Category")
axes[1].set_ylabel("Number of Stories")
axes[1].set_title("Stories per Category")
axes[1].tick_params(axis="x", rotation=30)


# Dashboard Chart 3
axes[2].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.7
)

axes[2].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    alpha=0.7
)

axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of Comments")
axes[2].set_title("Score vs Comments")
axes[2].legend()


# Add the overall dashboard title
fig.suptitle("TrendPulse Dashboard", fontsize=16)

plt.tight_layout()

# Save the complete dashboard
plt.savefig("outputs/dashboard.png")
plt.close()


# Tell us where the files were saved
print("Charts created successfully.")

print("Saved:")
print("outputs/chart1_top_stories.png")
print("outputs/chart2_categories.png")
print("outputs/chart3_scatter.png")
print("outputs/dashboard.png")
