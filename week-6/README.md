
# Week 6 – Edge Case Handling

## Project
College Rule-Based Chatbot

## Objective

The main objective of Week 6 is to improve the chatbot by handling different types of user inputs and edge cases.

The chatbot is designed to provide a suitable response even when the user enters an empty, invalid, unknown, or unrelated question.

## Tasks Completed

- Handled empty user input.
- Handled very short or incomplete questions.
- Added greeting detection.
- Handled unknown questions.
- Added a similarity threshold for detecting unrelated queries.
- Tested the chatbot with different types of inputs.
- Improved the chatbot so that it does not crash for unexpected inputs.

## Edge Cases Tested

| Input Type | Example | Expected Response |
|------------|---------|-------------------|
| Empty input | No input | Ask user to enter a question |
| Short input | `??` | Ask for a complete question |
| Greeting | `Hello` | Greeting response |
| Valid question | `Where is the library?` | Library information |
| Unknown question | `What is the weather?` | Information not available |
| Unrelated question | `Tell me a joke` | Information not available |

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Jupyter Notebook

## Files and Folders

```text
Week-6/
│
├── dataset/
│   ├── cleaned_college_faq.csv
│   └── intents.csv
│
├── notebooks/
│   └── edge_cases.ipynb
│
├── results/
│   └── edge_case_test_results.csv
│
├── src/
│   └── edge_case_handler.py
│
├── chatbot.py
├── requirements.txt
└── README.md
