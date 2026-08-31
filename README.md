# 📊 TrendPulse — Hacker News Trend Analysis

<div align="center">

**Turn trending stories into structured data, statistics, and visual insights.**

A four-stage Python data pipeline built around the Hacker News API.

**Collect → Process → Analyze → Visualize**

</div>

---

## 📌 Overview

**TrendPulse** is a Python-based data pipeline that collects trending stories from **Hacker News**, categorizes them using keyword matching, cleans the collected data, performs statistical analysis, and creates visualizations.

The project is designed as a complete end-to-end data workflow:

```text
Hacker News API
       │
       ▼
┌──────────────────────┐
│  1. Data Collection  │
│      JSON Output     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  2. Data Processing  │
│      Clean CSV       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    3. Data Analysis  │
│   Statistics & Data  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  4. Visualization    │
│     Charts & Trends  │
└──────────────────────┘
```

---

## 🎯 Project Objective

The goal of TrendPulse is to demonstrate how raw data from a public API can be transformed into useful information through a simple and understandable data pipeline.

The project covers:

- 🌐 API data collection
- 🗂️ Keyword-based categorization
- 🧹 Data cleaning
- 📄 JSON and CSV file handling
- 📈 Statistical analysis
- 📊 Data visualization
- 🔄 Multi-stage data processing

---

## 🧩 Project Tasks

### 1️⃣ Task 1 — Data Collection

**File:** `task1_data_collection.py`

The first stage collects trending stories from the Hacker News API.

Each usable story is categorized by checking whether its title contains predefined keywords.

### Categories

| Category | Example Keywords |
|---|---|
| 💻 Technology | AI, software, tech, code, cloud, API, GPU, LLM |
| 🌍 World News | war, government, president, election, climate, global |
| 🏆 Sports | NFL, NBA, FIFA, sport, team, player, league |
| 🔬 Science | research, study, space, physics, biology, NASA |
| 🎬 Entertainment | movie, film, music, Netflix, book, show, streaming |

The collected information includes:

- Post ID
- Story title
- Category
- Score
- Number of comments
- Author
- Collection timestamp

The raw data is saved as a dated JSON file inside `data/`.

---

### 2️⃣ Task 2 — Data Processing

**File:** `task2_data_processing.py`

The second stage prepares the collected data for analysis.

It:

- Finds the latest TrendPulse JSON file
- Loads the data using Pandas
- Removes duplicate posts
- Removes rows with missing important fields
- Converts score and comment values into numeric data
- Removes stories with scores below the required threshold
- Cleans unnecessary spaces from titles and author names
- Saves the cleaned dataset

**Output:**

```text
data/trends_clean.csv
```

---

### 3️⃣ Task 3 — Data Analysis

**File:** `task3_analysis.py`

The third stage uses Pandas and NumPy to understand the cleaned dataset.

The program calculates:

| Metric | Description |
|---|---|
| Average Score | Average score across collected stories |
| Average Comments | Average number of comments |
| Mean Score | Statistical mean of story scores |
| Median Score | Middle score in the dataset |
| Standard Deviation | Measures variation in story scores |
| Maximum Score | Highest story score |
| Minimum Score | Lowest story score |
| Category Counts | Number of stories in each category |
| Most Commented Story | Story with the highest comment count |

The resulting dataset is saved as:

```text
data/trends_analysed.csv
```

---

### 4️⃣ Task 4 — Data Visualization

**File:** `task4_visualization.py`

The final stage converts the data into visual insights using Matplotlib.

### 📈 Chart 1 — Top 10 Stories by Score

A horizontal bar chart showing the ten stories with the highest scores.

```text
outputs/chart1_top_stories.png
```

### 📊 Chart 2 — Stories per Category

A bar chart showing the number of stories collected in each category.

```text
outputs/chart2_categories.png
```

### 🔵 Chart 3 — Score vs Comments

A scatter plot comparing story scores with the number of comments. Stories are separated into **Popular** and **Not Popular** groups using a score threshold.

```text
outputs/chart3_scatter.png
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🌐 Requests | Sending API requests |
| 📦 JSON | Handling API data |
| 🐼 Pandas | Data loading, cleaning, and processing |
| 🔢 NumPy | Statistical calculations |
| 📊 Matplotlib | Creating charts |
| 📁 Glob | Finding matching data files |
| 💻 OS | Managing folders and file paths |

---

## 📂 Project Structure

```text
TrendPulse/
│
├── 📁 data/
│   ├── trends_20260828.json
│   ├── trends_20260829.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
│
├── 📁 outputs/
│   ├── chart1_top_stories.png
│   ├── chart2_categories.png
│   └── chart3_scatter.png
│
├── 🐍 task1_data_collection.py
├── 🐍 task2_data_processing.py
├── 🐍 task3_analysis.py
├── 🐍 task4_visualization.py
└── 📄 README.md
```

---

## ⚙️ Requirements

Make sure **Python 3** is installed.

Install the required Python packages:

```bash
pip install requests pandas numpy matplotlib
```

If your system uses `pip3`:

```bash
pip3 install requests pandas numpy matplotlib
```

---

## ▶️ How to Run

Run the four tasks in order because each stage uses the output from the previous stage.

### Step 1 — Collect the data

```bash
python3 task1_data_collection.py
```

This creates a dated JSON file inside `data/`.

### Step 2 — Clean the data

```bash
python3 task2_data_processing.py
```

This creates:

```text
data/trends_clean.csv
```

### Step 3 — Analyze the data

```bash
python3 task3_analysis.py
```

This creates:

```text
data/trends_analysed.csv
```

### Step 4 — Create visualizations

```bash
python3 task4_visualization.py
```

This creates the three chart images inside `outputs/`.

---

## 🔄 Data Flow

TrendPulse follows a clear sequence:

```text
Raw Hacker News Stories
          ↓
     JSON Dataset
          ↓
   Remove Duplicates
          ↓
    Handle Missing Data
          ↓
     Clean CSV Dataset
          ↓
   Statistical Analysis
          ↓
    Analysed Dataset
          ↓
      Visualizations
          ↓
     Trend Insights
```

---

## 📊 Example Analysis

A completed run of the project can produce statistics such as:

```text
Average score
Average comments
Mean score
Median score
Standard deviation
Maximum score
Minimum score
Most represented category
Most commented story
```

The exact values can change because Hacker News trending data changes over time.

---

## 💡 Key Insight

TrendPulse demonstrates that data analysis is more than collecting information.

The project takes data through the complete journey:

> **Collect it → clean it → understand it → visualize it.**

This makes the final information easier to explore and understand than the original raw API response.

---

## 🚀 Future Improvements

Possible extensions for TrendPulse include:

- Adding more news sources
- Improving category detection with NLP
- Tracking trends across multiple days
- Comparing category performance over time
- Adding interactive dashboards
- Storing historical datasets
- Creating automated trend reports

---

## 📚 Data Source

TrendPulse uses the public **Hacker News API** to retrieve story data.

No API key or user login is required for the endpoints used by this project.

---

## 👨‍💻 Project Information

**Project:** TrendPulse — What's Actually Trending Right Now

**Language:** Python

**Pipeline:** Data Collection → Data Processing → Data Analysis → Data Visualization

---

<div align="center">

### ⭐ TrendPulse

**Turning trending stories into meaningful insights.**

*Built with Python, Pandas, NumPy, Matplotlib, and the Hacker News API.*

</div>
