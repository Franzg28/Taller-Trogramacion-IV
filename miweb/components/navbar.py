import reflex as rx
from miweb.styles.styles import Size as Size
from miweb.styles.colors import TextColor as TexColor
from miweb.styles.colors import Color as Color
import miweb.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Franz Guaman Rivera",
            size="5",
            #font_family="Mona Sans",
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.BIG.value,
        z_index="999",
        top="0"
    )