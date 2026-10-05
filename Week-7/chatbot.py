from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# File paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
FAQ_PATH = BASE_DIR / "dataset" / "cleaned_college_faq.csv"

# -----------------------------
# Load FAQ dataset
# -----------------------------
df = pd.read_csv(FAQ_PATH)

print("FAQ dataset loaded!")
print("Columns:", df.columns.tolist())
print("Total FAQ questions:", len(df))

# -----------------------------
# Column names
# -----------------------------
QUESTION_COLUMN = "Question"
CATEGORY_COLUMN = "Expected Category" if "Expected Category" in df.columns else "Category"
ANSWER_COLUMN = "Answer" if "Answer" in df.columns else None

# -----------------------------
# Remove empty rows
# -----------------------------
subset_columns = [QUESTION_COLUMN, CATEGORY_COLUMN]
if ANSWER_COLUMN:
    subset_columns.append(ANSWER_COLUMN)

df = df.dropna(subset=subset_columns)

if ANSWER_COLUMN is None:
    df["Answer"] = df[CATEGORY_COLUMN].apply(
        lambda category: f"I can help with {category} questions."
    )
    ANSWER_COLUMN = "Answer"

questions = df[QUESTION_COLUMN].astype(str)
categories = df[CATEGORY_COLUMN].astype(str)

# -----------------------------
# TF-IDF
# -----------------------------
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X = vectorizer.fit_transform(questions)

# -----------------------------
# Naive Bayes
# -----------------------------
model = MultinomialNB()
model.fit(X, categories)

print("Model trained successfully!")

# -----------------------------
# Chatbot
# -----------------------------
def chatbot(user_input):

    if not user_input.strip():
        return "Please enter a question.", "Unknown", 0

    user_vector = vectorizer.transform([user_input])

    predicted_category = model.predict(user_vector)[0]

    similarities = cosine_similarity(
        user_vector,
        X
    )[0]

    best_index = similarities.argmax()
    best_score = similarities[best_index]

    # Unknown question
    if best_score < 0.25:
        return (
            "Sorry, I don't have information about that.",
            "Unknown",
            best_score
        )

    answer = df.iloc[best_index][ANSWER_COLUMN]

    return answer, predicted_category, best_score


# -----------------------------
# Run chatbot
# -----------------------------
print("\n==============================")
print("   WEEK 7 COLLEGE CHATBOT")
print("==============================")
print("Type 'exit' to stop.")

while True:

    try:
        user_input = input("\nYou: ")
    except EOFError:
        print("\nBot: Thank you! Goodbye.")
        break

    if user_input.lower().strip() == "exit":
        print("Bot: Thank you! Goodbye.")
        break

    answer, category, score = chatbot(user_input)

    print("Predicted Category:", category)
    print("Similarity Score:", round(score, 3))
    print("Bot:", answer)