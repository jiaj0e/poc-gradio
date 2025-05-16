# import reflex as rx

# # Common styles for questions and answers.
# shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
# chat_margin = "20%"
# message_style = dict(
#     padding="1em",
#     border_radius="5px",
#     margin_y="0.5em",
#     box_shadow=shadow,
#     max_width="30em",
#     display="inline-block",
# )

# # Set specific styles for questions and answers.
# question_style = message_style | dict(
#     margin_left=chat_margin,
#     background_color=rx.color("gray", 4),
# )
# answer_style = message_style | dict(
#     margin_right=chat_margin,
#     background_color=rx.color("accent", 8),
# )

# # Styles for the action bar.
# input_style = dict(
#     border_width="1px",
#     padding="0.5em",
#     box_shadow=shadow,
#     width="350px",
# )
# button_style = dict(
#     background_color=rx.color("accent", 10),
#     box_shadow=shadow,
# )


# Base styles
base_style = dict(
    padding="0",
    margin="0",
    box_sizing="border-box",
    font_family="Inter, system-ui, sans-serif",
)

# Message styles
message_style = dict(
    class_name="message",
    width="fit-content",
    max_width="70%",
    transition="all 0.2s ease",
)

question_style = message_style | dict(
    class_name="message question",
)

answer_style = message_style | dict(
    class_name="message answer",
)

# Input styles
input_style = dict(
    class_name="chat-input",
)

button_style = dict(
    class_name="send-button",
)

# Container styles
container_style = dict(
    class_name="chat-container",
)

action_bar_style = dict(
    class_name="input-container",
)
