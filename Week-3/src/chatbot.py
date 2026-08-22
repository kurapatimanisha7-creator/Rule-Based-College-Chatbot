import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# -----------------------------------
# 1. Load College FAQ Dataset
# -----------------------------------

DATASET_PATH = "dataset/cleaned_college_faq.csv"

df = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully!")
print("Total questions:", len(df))


# -----------------------------------
# 2. Prepare Data
# -----------------------------------

X = df["Question"].astype(str)
y = df["Category"].astype(str)


# -----------------------------------
# 3. Convert Text into TF-IDF
# -----------------------------------

tfidf = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X_tfidf = tfidf.fit_transform(X)

print("TF-IDF conversion completed!")
print("TF-IDF shape:", X_tfidf.shape)


# -----------------------------------
# 4. Train Naive Bayes Model
# -----------------------------------

model = MultinomialNB()

model.fit(X_tfidf, y)

print("Naive Bayes model trained successfully!")


# -----------------------------------
# 5. Start Chatbot
# -----------------------------------

print("\n===================================")
print("     COLLEGE QUERY CHATBOT")
print("===================================")

print("Ask questions about the college.")
print("Type 'exit' to stop the chatbot.\n")


while True:

    question = input("You: ")

    # Exit
    if question.lower() == "exit":
        print("Bot: Thank you! Goodbye!")
        break

    # Convert user question to TF-IDF
    question_vector = tfidf.transform([question])

    # Predict category
    predicted_category = model.predict(question_vector)[0]

    # Get probability
    probabilities = model.predict_proba(question_vector)[0]

    confidence = max(probabilities)

    print("Predicted Category:", predicted_category)
    print("Confidence:", round(confidence, 2))

    # Get answers from predicted category
    category_data = df[
        df["Category"] == predicted_category
    ]

    if len(category_data) > 0:

        answer = category_data.iloc[0]["Answer"]

        print("Bot:", answer)

    else:

        print(
            "Bot: Sorry, I could not find information "
            "for this question."
        )

    print()