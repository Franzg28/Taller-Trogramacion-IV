import reflex as rx

config = rx.Config(
    app_name="miweb",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)