#  Week 4 – Intent Design for College Rule-Based Chatbot

##  Project Overview

This project is the **Week 4** task of the College Rule-Based Chatbot .

The objective of this week is to design and define **user intents** so that the chatbot can understand the purpose of a student's question before searching the FAQ database.

Instead of directly matching every question, the chatbot first identifies the **intent** (such as Courses, Fees, Admission, Library, etc.) and then retrieves the relevant answer.

---

# 🎯 Week 4 Objective

- Learn the concept of **Intent Design**
- Define intents for college-related queries
- Create an intent dataset
- Build a rule-based intent detector
- Test intent prediction
- Improve chatbot understanding of user queries

---

# 🧠 What is Intent Design?

**Intent** is the purpose or meaning behind a user's question.

Example:

| Student Question | Intent |
|------------------|---------|
| Hello | Greeting |
| What courses are offered? | Courses |
| How much is the tuition fee? | Fees |
| How can I apply? | Admission |
| When are exams? | Examination |
| What are library timings? | Library |

Different questions with the same meaning are grouped into one intent.

Example:

**Intent = Courses**

- What courses are offered?
- Which programs are available?
- What B.Tech branches are available?
- Tell me about engineering courses.

All belong to the **Courses** intent.

---

# 📂 Project Structure

```text
Week-4/
│
├── dataset/
│   ├── cleaned_college_faq.csv
│   └── intents.csv
│
├── notebooks/
│   └── intent_design.ipynb
│
├── results/
│   ├── intent_distribution.png
│   └── intent_test_results.csv
│
├── src/
│   └── intent_detector.py
│
├── chatbot.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📁 Dataset Description

## 1. cleaned_college_faq.csv

Contains the cleaned FAQ dataset prepared in previous weeks.

**Columns**

- ID
- Category
- Question
- Answer

This file acts as the chatbot's knowledge base.

---

## 2. intents.csv

This is the new dataset created in Week 4.

**Columns**

| Column | Description |
|---------|-------------|
| intent | Category of the user's query |
| question | Example question representing that intent |

Example:

```csv
intent,question
courses,What courses are offered?
courses,Which programs are available?
fees,How much is tuition?
fees,What is the fee structure?
```

The dataset contains multiple question variations for each intent.

---

# 🏷️ Defined Intents

Ten major intents were created for the college chatbot.

| Intent | Purpose |
|----------|----------|
| Greeting | Greetings and conversation start |
| Admission | Admission process and eligibility |
| Courses | Programs and branches |
| Fees | Tuition and fee details |
| Examination | Exam schedule and timetable |
| Library | Library timings and services |
| Placement | Companies and placements |
| Faculty | Faculty information |
| Hostel | Hostel and accommodation |
| Campus | Campus facilities |

---

# ⚙️ Working Methodology

The chatbot follows the workflow below.

```text
User Question
      │
      ▼
Text Preprocessing
      │
      ▼
Intent Detection
      │
      ▼
Identify Intent
      │
      ▼
Filter Relevant FAQ Category
      │
      ▼
Find Best Matching Question
      │
      ▼
Return Answer
```

Example:

```text
User:
How much is the tuition fee?

↓

Detected Intent:
Fees

↓

Search Fees Category

↓

Return Fee Information
```

---

# 💻 Implementation

## Step 1 – Create Intent Dataset

Created `intents.csv` containing:

- 10 intents
- Multiple question variations
- Balanced examples for each intent

---

## Step 2 – Analyze Intent Dataset

Using **Pandas**, the dataset was analyzed to identify:

- Total questions
- Total intents
- Questions per intent
- Intent distribution

Example Python:

```python
import pandas as pd

df = pd.read_csv("../dataset/intents.csv")

print(df["intent"].value_counts())
```

---

## Step 3 – Visualize Intent Distribution

A bar chart was generated using **Matplotlib**.

Output file:

```text
results/intent_distribution.png
```

This helps verify that each intent contains sufficient training examples.

---

## Step 4 – Rule-Based Intent Detection

The file:

```text
src/intent_detector.py
```

contains the rule-based intent detection logic.

Example:

```python
if any(word in text for word in ["course","program","branch"]):
    return "courses"
```

Similarly, keywords are defined for all ten intents.

---

## Step 5 – Chatbot Integration

`chatbot.py` combines:

- Intent Detection
- FAQ Dataset
- Answer Retrieval

Workflow:

```text
Input Question
      ↓
Detect Intent
      ↓
Select Category
      ↓
Search FAQ
      ↓
Display Answer
```

---

# 🧪 Testing

Sample test cases:

| User Question | Predicted Intent |
|--------------|-----------------|
| Hello | Greeting |
| What courses are offered? | Courses |
| How much is tuition? | Fees |
| How can I apply? | Admission |
| When are exams? | Examination |
| Library timings | Library |
| Companies visiting campus | Placement |
| Is hostel available? | Hostel |

The testing results are stored in:

```text
results/intent_test_results.csv
```

---

# 📊 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Handling |
| Matplotlib | Data Visualization |
| Jupyter Notebook | Development & Testing |
| VS Code | Code Editor |
| CSV | Dataset Storage |
| Git & GitHub | Version Control |

---

# 📦 Python Libraries

```text
pandas
matplotlib
scikit-learn
jupyter
```

Install using:

```bash
pip install -r requirements.txt
```

---

# 📚 Concepts Learned

During Week 4, the following concepts were learned:

- Intent Design
- Intent Definition
- Question Categorization
- Rule-Based NLP
- Dataset Creation
- Data Visualization
- Intent Testing
- Modular Python Programming
- CSV Data Processing
- Chatbot Query Classification

---

# 🎓 Learning Outcomes

After completing Week 4, I was able to:

- Design intents for conversational AI systems.
- Define multiple user intents for a college chatbot.
- Create an intent dataset with question variations.
- Implement a rule-based intent detector.
- Analyze intent distribution using Python.
- Visualize dataset statistics with Matplotlib.
- Organize chatbot modules into reusable Python files.
- Improve chatbot understanding before FAQ matching.
- Prepare the chatbot for advanced NLP integration.
- Strengthen practical knowledge of chatbot architecture.

---

# ✅ Tasks Completed

- Created Week 4 project structure
- Added cleaned FAQ dataset
- Created `intents.csv`
- Defined 10 chatbot intents
- Added multiple questions for each intent
- Built `intent_design.ipynb`
- Analyzed intent dataset
- Generated intent distribution graph
- Implemented `intent_detector.py`
- Built integrated `chatbot.py`
- Tested intent prediction
- Documented the complete workflow

---

# 🔄 Week Progression

```text
Week 1
Data Collection & Cleaning
          │
          ▼
Week 2
Rule-Based Chatbot
          │
          ▼
Week 3
ML-Based Chatbot & Evaluation
          │
          ▼
Week 4
Intent Design & Intent Detection
```

Week 4 introduces an additional **Intent Detection Layer** before searching the FAQ database, making the chatbot more organized and accurate.

---

# 🚀 Future Enhancements

- Add more college-specific intents
- Handle spelling mistakes
- Add synonym recognition
- Implement TF-IDF intent classification
- Use Machine Learning for intent prediction
- Add confidence score for predictions
- Integrate RAG with college website
- Support multilingual queries
- Improve unknown intent handling
- Deploy chatbot as a web application

---

# 👩‍💻 Author

**Project:** College Rule-Based Chatbot

**Week:** 4

**Learning Topic:** Intent Design

**Task:** Define Intents

**Language:** Python
