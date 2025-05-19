import reflex as rx

from reflex_app import style
from reflex_app.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="0.5em",
        display="flex",
        flex_direction="column",
        align_items="flex-end",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        ),
        style={"flex": "1 1 auto", "overflow_y": "auto", "min_height": "320px"},
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            on_key_down=lambda key: rx.cond(
                (key == "Enter") & (State.question != ""),  # Ensure question is not empty
                State.answer(),
                None,  # False branch: Do nothing
            ),
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=rx.cond(
                State.question != "",  # Ensure question is not empty
                State.answer(),  # True branch: Trigger State.answer()
                None,  # False branch: Do nothing
            ),
            style=style.button_style,
        ),
        style=style.action_bar_style,
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.foreach(
                State.chats,
                lambda chat, idx: rx.button(
                    chat.name,
                    on_click=lambda idx=idx: State.select_chat(idx),
                    style={
                        "background_color": rx.cond(
                            State.current_chat == idx,
                            style.PRIMARY_GREEN,
                            style.LIGHT_GREEN,
                        ),
                        "color": rx.cond(
                            State.current_chat == idx,
                            "#fff",
                            style.PRIMARY_GREEN,
                        ),
                        "border": style.sidebar_button_border,
                        "border_radius": style.sidebar_button_radius,
                        "padding": style.sidebar_button_padding,
                        "margin_bottom": style.sidebar_button_margin_bottom,
                        "font_weight": style.sidebar_button_font_weight,
                        "cursor": style.sidebar_button_cursor,
                        "transition": style.sidebar_button_transition,
                    },
                ),
            ),
            rx.button(
                "+ New Chat",
                on_click=State.new_chat,
                style=style.new_chat_button_style,
            ),
            style=style.sidebar_style,
        ),
        style=style.sidebar_container_style,
    )


def index() -> rx.Component:
    return rx.center(
        rx.hstack(
            sidebar(),
            rx.vstack(
                rx.box(
                    chat(),
                    style=style.container_style,
                ),
                action_bar(),
                style={"width": "100%", "max_width": "480px"},
            ),
            align_items="flex-start",
            width="100%",
            padding="2em 0",
        ),
        width="100vw",
        min_height="100vh",
        style=style.base_style,
    )


app = rx.App(
    stylesheets=[],
)
app.add_page(index)
