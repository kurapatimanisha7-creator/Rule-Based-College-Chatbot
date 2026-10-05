




# Week 7 – Testing and Refinement

## Project
College Rule-Based Chatbot

## Objective

The main objective of Week 7 is to test the chatbot with different user questions, identify incorrect responses, and improve the chatbot's accuracy and reliability.

## Tasks Completed

- Created a set of test questions.
- Tested different types of college-related queries.
- Tested different ways of asking the same question.
- Compared expected and predicted categories.
- Checked similarity scores.
- Identified incorrect predictions.
- Improved FAQ data for commonly confused questions.
- Tested the chatbot again after refinement.
- Generated final testing results.

## Testing Categories

The chatbot was tested with questions related to:

- Admission
- Courses
- Campus
- Examination
- Faculty
- Fees
- Greeting
- Hostel
- Library
- Placement
- Unknown questions

## Example Testing

| User Question | Expected Category | Predicted Category | Status |
|---------------|-------------------|--------------------|--------|
| What courses are offered? | Courses | Courses | Pass |
| Where is the library? | Library | Library | Pass |
| What are the hostel facilities? | Hostel | Hostel | Pass |
| When are examinations? | Examination | Examination | Pass |
| What are the placement opportunities? | Placement | Placement | Pass |
| What is the weather today? | Unknown | Unknown | Pass |

## Testing Process

```text
User Question
      ↓
Text Preprocessing
      ↓
TF-IDF Transformation
      ↓
Category Prediction
      ↓
FAQ Similarity Matching
      ↓
Best Matching Answer
      ↓
Testing Result
      ↓
Identify Errors
      ↓
Improve Dataset / Code
      ↓
Retest
