import reflex as rx
from miweb.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button(
            "ACCION",
            "Estas són peliculas de acción, para todo público",
            "https://www.netflix.com"),
        link_button(
            "DRAMA",
            "Estas són peliculas de drama",
            "https://github.com/"),
        link_button(
            "COMEDIA",
            "Estas són peliculas de comedia",
            "https://www.google.com/"),
        link_button(
            "TERROR",
            "Estas són peliculas de terror",
            "https://www.youtube.com/"),
        width="100%"
    
    
    )   