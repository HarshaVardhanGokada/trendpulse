import requests
import json
import os
import time
from datetime import datetime


# HackerNews gives us the IDs of the currently trending stories.
TOP_STORIES_URL = (
    "https://hacker-news.firebaseio.com/v0/topstories.json"
)

HEADERS = {
    "User-Agent": "TrendPulse/1.0"
}


# These are the categories and the words used to identify them.
categories = {
    "technology": [
        "ai", "software", "tech", "code", "computer",
        "data", "cloud", "api", "gpu", "llm"
    ],

    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],

    "sports": [
        "nfl", "nba", "fifa", "sport", "game",
        "team", "player", "league", "championship"
    ],

    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "nasa", "genome"
    ],

    "entertainment": [
        "movie", "film", "music", "netflix", "game",
        "book", "show", "award", "streaming"
    ]
}


def title_matches_category(title, keywords):
    """
    Check whether at least one category keyword
    appears in the story title.
    """
    title = title.lower()

    for keyword in keywords:
        if keyword in title:
            return True

    return False


def fetch_story(story_id):
    """
    Fetch one story from HackerNews.
    If the request fails, return None instead of
    stopping the complete program.
    """

    story_url = (
        f"https://hacker-news.firebaseio.com/v0/"
        f"item/{story_id}.json"
    )

    try:
        response = requests.get(
            story_url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print(
            f"Could not fetch story {story_id}: {error}"
        )
        return None


def main():

    # First get the list of the top 500 story IDs.
    try:
        response = requests.get(
            TOP_STORIES_URL,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        story_ids = response.json()[:500]

    except requests.RequestException as error:
        print(
            f"Could not fetch the top story list: {error}"
        )
        return


    all_collected_stories = []

    # Keep track of story IDs that have already been saved.
    used_story_ids = set()


    # Process one category at a time.
    for category, keywords in categories.items():

        category_count = 0

        for story_id in story_ids:

            # Stop once this category has 25 stories.
            if category_count >= 25:
                break

            # Avoid saving the same story twice.
            if story_id in used_story_ids:
                continue

            story = fetch_story(story_id)

            if story is None:
                continue

            # We only need stories that actually have a title.
            title = story.get("title")

            if not title:
                continue

            # Check the title against this category's keywords.
            if not title_matches_category(title, keywords):
                continue

            record = {
                "post_id": story.get("id"),
                "title": title,
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get(
                    "descendants", 0
                ),
                "author": story.get(
                    "by", "unknown"
                ),
                "collected_at": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }

            all_collected_stories.append(record)
            used_story_ids.add(story_id)
            category_count += 1

        print(
            f"{category}: {category_count} stories"
        )

        # The assignment asks for a 2-second delay
        # between category loops.
        time.sleep(2)


    # Create the data folder if it does not already exist.
    os.makedirs("data", exist_ok=True)


    # Create today's JSON filename.
    date_text = datetime.now().strftime("%Y%m%d")

    output_file = (
        f"data/trends_{date_text}.json"
    )


    # Save all collected stories.
    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            all_collected_stories,
            file,
            indent=2,
            ensure_ascii=False
        )


    print(
        f"\nCollected {len(all_collected_stories)} stories. "
        f"Saved to {output_file}"
    )


if __name__ == "__main__":
    main()