import reflex as rx


def render_socials(title: str, socials: list[str, str]):
    """Developer Social Media Bio.

    Args:
        title (str): Name of the social media
        socials (list[str, str]): A list of social media svg path

    Returns:
        rx.vstack: Returns a list of the developer's social media.
    """
    return rx.vstack(
        rx.text(title, font_weight="bolder"),
        rx.hstack(
            *[
                rx.link(
                    rx.image(
                        src=source,
                        html_width="16px",
                        html_height="16px",
                        color="white",
                    ),
                    href=link,
                )
                for source, link in socials
            ],
            width="100%",
            display="flex",
            justify_content="start",
            align_items="end",
            spacing="7",
        ),
        spacing="3",
        padding=["2em 2em", "2em 2em", "2em 2em", "2em 5em", "2em 5em"],
    )
