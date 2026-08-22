# 🤖 Week 3 – ML-Based College Query Chatbot

## 📌 Overview

Week 3 focuses on applying Natural Language Processing (NLP) and Machine Learning techniques to improve the College Rule-Based Chatbot.

The chatbot is designed to understand college-related questions, identify the appropriate category, and retrieve the corresponding answer from the college FAQ dataset.

In this week, traditional text-matching is enhanced using:

- Text Preprocessing
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Train-Test Split
- Classification Evaluation
- Confusion Matrix
- Interactive Chatbot Testing

---

## 🎯 Objectives

The main objectives of Week 3 are:

1. Understand basic text preprocessing techniques.
2. Convert textual questions into numerical features using TF-IDF.
3. Train a Multinomial Naive Bayes classification model.
4. Predict the category of a user's college-related question.
5. Retrieve the appropriate answer from the FAQ dataset.
6. Evaluate the performance of the trained model.
7. Build an interactive chatbot for testing college queries.

---

## 🏫 Project Context

### Project Title

**Rule-Based College Chatbot**

The chatbot provides answers to frequently asked questions related to college facilities, admissions, courses, examinations, placements, fees, hostel, library, faculty, and other campus-related information.

Instead of relying only on exact keyword matching, Week 3 introduces Machine Learning-based text classification to understand the intent/category of a user question.

---

# 🔄 System Workflow

```text
             User Question
                   ↓
          Text Preprocessing
                   ↓
             TF-IDF Vectorizer
                   ↓
       Multinomial Naive Bayes
                   ↓
        Predict Question Category
                   ↓
        Retrieve Matching FAQ
                   ↓
          Generate Chatbot Answer
                   ↓
             Display Response
