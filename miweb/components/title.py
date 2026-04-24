import reflex as rx
import miweb.styles.styles as styles

def title(text:str)-> rx.Component:
    return rx.heading(
                text,
                #size="9",
                style=styles.title_style
        
    )

