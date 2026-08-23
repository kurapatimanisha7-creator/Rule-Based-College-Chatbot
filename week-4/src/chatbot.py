import pandas as pd
import sys

# Add src folder to Python path
sys.path.append("src")

from intent_detector import detect_intent


# Load FAQ dataset
faq_df = pd.read_csv("dataset/cleaned_college_faq.csv")


def find_answer(user_question, intent):
    """
    Find the most relevant FAQ answer
    based on the detected intent.
    """

    # Filter FAQs according to detected intent/category
    relevant_faqs = faq_df[
        faq_df["Category"].str.lower() == intent.lower()
    ]

    # If no FAQ category is found
    if relevant_faqs.empty:
        return "Sorry, I could not find information for this topic."

    # Check for an exact question match
    for _, row in relevant_faqs.iterrows():

        if user_question.lower() == str(row["Question"]).lower():
            return row["Answer"]

    # Simple keyword matching
    user_words = set(user_question.lower().split())

    best_answer = None
    best_score = 0

    for _, row in relevant_faqs.iterrows():

        faq_question = str(row["Question"]).lower()
        faq_words = set(faq_question.split())

        score = len(user_words.intersection(faq_words))

        if score > best_score:
            best_score = score
            best_answer = row["Answer"]

    if best_answer:
        return best_answer

    return "Sorry, I could not find a suitable answer."


def chatbot():

    print("======================================")
    print("      College Rule-Based Chatbot")
    print("======================================")
    print("Type 'exit' to stop the chatbot.")
    print()

    while True:

        user_question = input("You: ")

        if user_question.lower() == "exit":
            print("Bot: Thank you! Goodbye.")
            break

        # Detect user's intent
        intent = detect_intent(user_question)

        print("Detected Intent:", intent)

        # Handle unknown intent
        if intent == "unknown":
            print("Bot: Sorry, I could not understand your question.")
            print()
            continue

        # Find answer using the detected intent
        answer = find_answer(user_question, intent)

        print("Bot:", answer)
        print()


if __name__ == "__main__":
    chatbot()