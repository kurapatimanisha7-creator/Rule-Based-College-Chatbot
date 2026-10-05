def handle_edge_case(user_input):

    # Empty input
    if not user_input.strip():
        return "Please enter a question."

    # Very short input
    if len(user_input.strip()) < 3:
        return "Please enter a complete question."

    # Unknown / unrelated question
    if user_input.lower() in ["hello", "hi", "hey"]:
        return "Hello! Welcome to the College Query Chatbot."

    return None