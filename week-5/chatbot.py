import pandas as pd
import sys

sys.path.append("src")

from intent_detector import detect_intent
from conversation_state import ConversationState
from context_handler import resolve_context


# Load FAQ dataset
faq_df = pd.read_csv("dataset/cleaned_college_faq.csv")

# Create conversation state
state = ConversationState()


def find_answer(user_question, intent):

    relevant_faqs = faq_df[
        faq_df["Category"].str.lower() == intent.lower()
    ]

    if relevant_faqs.empty:
        return "Sorry, I could not find information about this topic."

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

    return relevant_faqs.iloc[0]["Answer"]


def chatbot():

    print("=" * 45)
    print("       COLLEGE CONVERSATIONAL CHATBOT")
    print("=" * 45)

    print("Type 'reset' to clear conversation.")
    print("Type 'history' to view conversation history.")
    print("Type 'exit' to end the chatbot.")
    print()

    while True:

        user_question = input("You: ").strip()

        # Exit
        if user_question.lower() == "exit":
            print("Bot: Thank you for using the College Chatbot!")
            break

        # Reset
        if user_question.lower() == "reset":
            state.reset()
            print("Bot: Conversation has been reset.")
            print()
            continue

        # History
        if user_question.lower() == "history":

            history = state.get_history()

            if not history:
                print("Bot: No conversation history available.")
            else:
                print("\nConversation History:")

                for item in history:
                    print(
                        "Question:",
                        item["question"],
                        "| Intent:",
                        item["intent"]
                    )

            print()
            continue

        # Detect intent
        intent = detect_intent(user_question)

        # Try context handling for follow-up questions
        context_intent = resolve_context(
            user_question,
            state.get_last_intent()
        )

        if context_intent:
            intent = context_intent

        # Update conversation state
        state.update(intent, user_question)

        # Unknown question
        if intent == "unknown":
            print(
                "Bot: Sorry, I could not understand your question."
            )
            print()
            continue

        # Find answer
        answer = find_answer(user_question, intent)

        print("Bot:", answer)

        print(
            "Current Intent:",
            state.get_last_intent()
        )

        print()


if __name__ == "__main__":
    chatbot()