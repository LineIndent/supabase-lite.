import reflex as rx

HEADER: dict = {
    "width": "100%",
    "padding": ["1em 2em", "1em 2em", "1em 4em", "1em 4em", "1em 4em"],
    "border_bottom": "1px solid #404040",
}


theme_button = rx.button(
    rx.color_mode_cond(
        rx.icon(tag="moon"),
        rx.icon(tag="sun"),
    ),
    variant="ghost",
    transform="scale(0.8)",
)


def render_header():
    """The header component.

    Returns:
        rx.Hstack: The UI component for header.
    """
    BASE_FONT: int = 12

    return rx.hstack(
        rx.heading(
            "Supabase API Client",
            font_size=[f"{BASE_FONT * (1.2**index)}px" for index in range(5)],
            transition="all 550ms ease",
        ),
        rx.spacer(),
        style=HEADER,
    )
