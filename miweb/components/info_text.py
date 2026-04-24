import reflex as rx
from miweb.styles.styles import Size as Style
from miweb.styles.colors import Color as Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.el.span(
            title,
            font_weight="Time New Roman",
            color=Color.SECONDARY.value,
            ),
        f" {body}",font_size=Style.MEDIUM.value
    )