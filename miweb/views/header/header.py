import reflex as rx
from miweb.components.link_icon import link_icon
from miweb.components.info_text import info_text
from miweb.styles.colors import TextColor as TexColor
from miweb.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.avatar(fallback="FGR",size="5",color_scheme="orange",variant="solid"),
        rx.vstack(
            rx.text("@Franz"),
            rx.text("Software Engineer"),
            color=TexColor.BODY.value,
            margin_top=Size.ZERO.value            

        )
            
        ),
        
        rx.hstack(
            link_icon("https://www.google.com"),
            link_icon("https://www.google.com"),
            link_icon("https://www.google.com"),
            link_icon("https://www.google.com"),
            align="start",
            spacing="3",
         ),
        rx.flex(
            info_text("Titulo","Este es el cuerpo"),
            #rx.Spacer(),
            info_text("Titulo","Este es el cuerpo"),
            #rx.Spacer(),
            info_text("Titulo","Este es el cuerpo"),
            spacing="8",
            wodth="100%",
            

        ), 
        rx.text("Esta es una página web de prueba, vamos a realizar una réplica de GitHub"),
        
        
    ),
    