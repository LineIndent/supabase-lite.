import reflex as rx


BASE_FONT: int = 16


def render_title():
    """Web Application Title

    Returns:
        rx.heading: Sets the webpage title.
    """
    return rx.heading(
        "Supabase API Client",
        font_size=[f"{BASE_FONT * (1.2**index)}px" for index in range(5)],
        transition="all 550ms ease",
        id="client",
    )
