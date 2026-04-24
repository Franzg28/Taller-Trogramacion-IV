import reflex as rx
import datetime
from miweb.components.link_icon import link_icon
import miweb.styles.styles as styles
from miweb.styles.styles import Size
from miweb.styles.colors import TextColor as TexColor

def footer() -> rx.Component:
    return rx.vstack(
        
        rx.image(src="/favicon.ico"),
        rx.link(
            f"Este es un proyecto reservado - {datetime.date.today().year}",
            font_size=Size.BIG.value,
            href="https://www.entel.bo/",
            is_external=True,
            color=TexColor.FOOTER.value,
            
        ),
        rx.text("Copyright © 2027 Franz"),
        font_size=Size.MEDIUM.value,
        margin_bottom=Size.VBIG.value,
        align="center",
        color=TexColor.FOOTER.value,
        padding_bottom=Size.VBIG.value
         

    )