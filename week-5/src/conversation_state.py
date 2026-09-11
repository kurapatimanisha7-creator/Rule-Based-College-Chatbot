class ConversationState:

    def __init__(self):
        self.last_intent = None
        self.last_question = None
        self.history = []

    def update(self, intent, question):

        self.last_intent = intent
        self.last_question = question

        self.history.append({
            "question": question,
            "intent": intent
        })

    def get_last_intent(self):
        return self.last_intent

    def get_last_question(self):
        return self.last_question

    def get_history(self):
        return self.history

    def reset(self):
        self.last_intent = None
        self.last_question = None
        self.history = []