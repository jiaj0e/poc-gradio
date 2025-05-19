import reflex as rx

from reflex_app.agent import ask


class ChatSession(rx.Base):
    name: str
    chat_history: list[tuple[str, str]]


class State(rx.State):
    # List of chat sessions
    chats: list[ChatSession] = [ChatSession(name="Chat 1", chat_history=[])]
    # Index of the currently selected chat
    current_chat: int = 0
    # The current question being asked.
    question: str = ""
    # The chat history of the currently selected chat
    chat_history: list[tuple[str, str]] = []
    # The current response being streamed.
    current_response: str = ""

    @rx.event
    def select_chat(self, idx: int):
        self.current_chat = idx
        self.chat_history = self.chats[idx].chat_history

    @rx.event
    async def answer(self):
        """
        Handle the streaming response and update the chat history dynamically.
        """
        self.current_response = ""
        self.chat_history.append((self.question, ""))
        async for chunk in ask(self.question):
            self.current_response += chunk  # Append the streamed chunk to the response
            self.chat_history[-1] = (self.question, self.current_response)  # Update the chat history
            yield  # Yield to update the UI dynamically
        self.question = ""  # Clear the question input
        yield

    @rx.event
    def new_chat(self):
        chat_num = len(self.chats) + 1
        new_chat = ChatSession(name=f"Chat {chat_num}", chat_history=[])
        self.chats.append(new_chat)
        self.select_chat(len(self.chats) - 1)
