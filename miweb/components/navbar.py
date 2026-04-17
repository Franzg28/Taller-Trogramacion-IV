import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Franz Guaman Rivera",
            size="5"
        ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index="999"
    )