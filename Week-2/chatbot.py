import pandas as pd

# Load FAQ dataset
df = pd.read_csv("cleaned_college_faq.csv")


# Preprocess text
def preprocess_text(text):
    return str(text).lower().strip()


df["Question"] = df["Question"].apply(preprocess_text)


# Rule-based chatbot
def chatbot(user_question):

    user_question = preprocess_text(user_question)

    # Exact matching
    for index, question in enumerate(df["Question"]):
        if user_question == question:
            return df.iloc[index]["Answer"]

    # Keyword rules
    keywords = {
        "library": "Library",
        "book": "Library",
        "books": "Library",

        "admission": "Admission",
        "apply": "Admission",
        "eligibility": "Admission",

        "course": "Courses",
        "courses": "Courses",
        "branch": "Courses",

        "placement": "Placement",
        "placements": "Placement",
        "job": "Placement",

        "fee": "Fees",
        "fees": "Fees",
        "scholarship": "Fees",

        "exam": "Examination",
        "exams": "Examination",
        "examination": "Examination",

        "hostel": "Hostel",
        "room": "Hostel",
        "rooms": "Hostel",

        "faculty": "Faculty",
        "teacher": "Faculty",
        "teachers": "Faculty",

        "campus": "Campus",

        "hi": "Greeting",
        "hello": "Greeting",
        "hey": "Greeting"
    }

    for keyword, category in keywords.items():

        if keyword in user_question:

            category_data = df[
                df["Category"].str.lower() == category.lower()
            ]

            if not category_data.empty:
                return category_data.iloc[0]["Answer"]

    return "Sorry, I couldn't understand your question."


# Start chatbot
print("====================================")
print("       COLLEGE QUERY CHATBOT")
print("====================================")
print("Type 'bye' to exit.")

while True:

    user_question = input("You: ")

    if user_question.lower().strip() == "bye":
        print("Bot: Thank you! Have a nice day.")
        break

    print("Bot:", chatbot(user_question))