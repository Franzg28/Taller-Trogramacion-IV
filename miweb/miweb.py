import reflex as rx
from miweb.components.navbar import navbar
from miweb.views.header.header import header
from miweb.views.links.links import links
from miweb.components.footer import footer
import miweb.styles.styles as styles
from miweb.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=Size.BIG.value,
            align="center"
        )

        ),
        footer()
        
      )
    

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=["https://fonts.googleapis.com/css2?family=Mona+Sans:ital,wght@0,200..900;1,200..900&display=swap"
                 ]
)
app.add_page(index)