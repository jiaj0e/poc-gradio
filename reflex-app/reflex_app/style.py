# Minimalistic, green-based color palette
PRIMARY_GREEN = "#27ae60"
LIGHT_GREEN = "#eafaf1"
DARK_GREEN = "#145a32"
BORDER_COLOR = "#b7e4c7"
TEXT_COLOR = "#222"

# Base styles
base_style = dict(
    padding="0",
    margin="0",
    box_sizing="border-box",
    font_family="Inter, system-ui, sans-serif",
    background_color=LIGHT_GREEN,
    color=TEXT_COLOR,
)

# Message styles
message_style = dict(
    padding="0.7em 1em",
    border_radius="12px",
    margin_y="0.4em",
    max_width="90%",
    font_size="1em",  # Increased font size for larger text
    box_shadow="none",
    border=f"1px solid {BORDER_COLOR}",
)

question_style = message_style | dict(
    background_color="#fff",
    color=PRIMARY_GREEN,
    align_self="flex-end",
    border=f"1.5px solid {PRIMARY_GREEN}",
)

answer_style = message_style | dict(
    background_color=PRIMARY_GREEN,
    color="#fff",
    align_self="flex-start",
    border="none",
)

# Input styles
input_style = dict(
    border=f"1.5px solid {PRIMARY_GREEN}",
    border_radius="10px",
    font_size="1em",
    background_color="#fff",
    color=TEXT_COLOR,
    outline="none",
    width="100%",
)

button_style = dict(
    background_color=PRIMARY_GREEN,
    color="#fff",
    border="none",
    border_radius="10px",
    padding="0.6em 1.2em",
    font_weight="600",
    font_size="1em",
    cursor="pointer",
    transition="background 0.2s",
    _hover={"background_color": DARK_GREEN},
)

# Container styles
container_style = dict(
    background_color="#fff",
    border_radius="16px",
    box_shadow="0 2px 12px rgba(39, 174, 96, 0.08)",
    padding="2em 1.2em 1em 1.2em",
    max_width="720px",
    min_width="520px",
    margin="2em auto",
    display="flex",
    flex_direction="column",
    gap="1.2em",
)

action_bar_style = dict(
    display="flex",
    gap="0.5em",
    margin_top="1em",
    width="100%",
    justify_content="center",
)

sidebar_style = dict(
    background_color=LIGHT_GREEN,
    padding="1em 0.5em",
    min_width="160px",
    border_radius="12px",
    box_shadow="0 1px 4px rgba(39, 174, 96, 0.04)",
    display="flex",
    flex_direction="column",
    gap="0.5em",
)

# Sidebar button styles
sidebar_button_border = f"1.5px solid {PRIMARY_GREEN}"
sidebar_button_radius = "8px"
sidebar_button_padding = "0.5em 1em"
sidebar_button_margin_bottom = "0.3em"
sidebar_button_font_weight = "600"
sidebar_button_cursor = "pointer"
sidebar_button_transition = "background 0.2s"

# New chat button style
new_chat_button_style = dict(
    background_color="#fff",
    color=PRIMARY_GREEN,
    border=f"1.5px dashed {PRIMARY_GREEN}",
    border_radius="8px",
    padding="0.5em 1em",
    font_weight="600",
    cursor="pointer",
    margin_top="1em",
)

# Sidebar container style
sidebar_container_style = dict(
    min_width="180px",
    margin_right="2em",
)

# Styles for API-related messages (if needed for agent.py)
api_error_style = dict(
    color="red",
    font_weight="bold",
)

api_success_style = dict(
    color="green",
    font_weight="bold",
)

# Add any other centralized styles here as needed.
