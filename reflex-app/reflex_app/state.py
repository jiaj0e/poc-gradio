import reflex as rx

from reflex_app.agent import ask


class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    @rx.event
    async def answer(self):
        # Our chatbot is not very smart right now...
        answer = ""
        self.chat_history.append((self.question, ""))

        print("Asking:", self.question)
        answer = ask(self.question)
        print("Answer:", answer)
        self.chat_history[-1] = (
            self.chat_history[-1][0],
            answer,
        )
        yield

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield
