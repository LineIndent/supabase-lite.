import reflex as rx

HEADER: dict = {
    "width": "100%",
    "padding": "1em 2em",
    "border_bottom": "1px solid #404040",
}


theme_button = rx.button(
    rx.color_mode_cond(
        rx.icon(tag="moon"),
        rx.icon(tag="sun"),
    ),
    variant="ghost",
    # on_click=rx.toggle_color_mode,
    transform="scale(0.8)",
)


def render_header():
    """The header component.

    Returns:
        rx.Hstack: The UI component for header.
    """
    return rx.hstack(
        rx.spacer(),
        theme_button,
        style=HEADER,
    )
