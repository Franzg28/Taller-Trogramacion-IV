from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#constantes
MAX_WIDTH="600px"

#tamaños
class Size(Enum):
    ZERO="0em"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"
    VBIG="3em"

navbar_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.BIG.value

)

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.PRIMARY.value,
    rx.button:{
        "width": "100%",
        "height": "100%",
        "display":"block",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "color": TextColor.FOOTER.value,
        "background_color": Color.SECONDARY.value,
        "_hover":{
            "background_color": Color.BACKGROUND.value,
        }
            
        
    },
    rx.link:{
        "text_decoration":"none"
    }

 }
title_style = dict(
    font_size= Size.BIG.value,
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.FOOTER.value
)

button_title_styles = dict(
        font_size = Size.DEFAULT.value
)
button_body_styles = dict(
    font_size = Size.MEDIUM.value
)

