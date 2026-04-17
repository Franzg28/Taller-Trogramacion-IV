import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="FGR",size="5",color_scheme="orange",variant="solid"),
        rx.text("@Franz"),
        rx.text("Software Engineer"),
        align="center"
    )