def resolve_context(user_question, last_intent):

    question = user_question.lower()

    follow_up_words = [
        "what about",
        "how about",
        "and fees",
        "and hostel",
        "and placements"
    ]

    if any(word in question for word in follow_up_words):

        if "fee" in question or "fees" in question:
            return "fees"

        if "hostel" in question:
            return "hostel"

        if "placement" in question or "placements" in question:
            return "placement"

        if last_intent:
            return last_intent

    return None