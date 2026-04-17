import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.text("Copyright © 2027 Franz"),
        rx.image(src="/favicon.ico"),
        rx.link(
            f"Este es un proyecto reservado - {datetime.date.today().year}",
            href="https://www.entel.bo/",
            is_external=True
        )
    )