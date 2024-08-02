import reflex as rx

from ..components.navbar import render_navbar
from ..components.output import render_output_box
from ..components.input import render_input_box


DOTS: dict = {
    "@keyframes dots": {
        "0%": {"background_position": "0 0"},
        "100%": {"background_position": "40px 40px"},
    },
    "animation": "dots 4s linear infinite",
}

CLIENT: dict[str, str] = {
    "width": "100%",
    "display": "flex",
    "justify_content": "start",
    "align_items": "start",
    "title_and_status": {
        "width": "100%",
        "display": "flex",
        "flex_wrap": ["wrap-reverse", "wrap-reverse", "wrap-reverse", "wrap", "wrap"],
        "justify_content": "space-between",
        "align_items": "center",
        "gap": "1em 0.4em",
        "padding": ["2em 2em", "2em 2em", "2em 4em", "2em 4em", "2em 4em"],
    },
    "data_boxes": {
        "width": "100%",
        "display": "flex",
        "align_items": "start",
        "justify_content": "start",
        "flex_wrap": [
            "wrap-reverse",
            "wrap-reverse",
            "wrap-reverse",
            "wrap-reverse",
            "wrap",
        ],
        "padding": "2em",
    },
}


@rx.page("/")
def client() -> rx.Component:
    """The client page.
    Returns:
        The UI for the client page.
    """

    return rx.vstack(
        render_navbar(),
        rx.hstack(
            render_input_box(),
            render_output_box(),
            spacing="6",
            style=CLIENT.get("data_boxes"),
        ),
        style=CLIENT,
        background="#161718",
        width="100%",
        min_height="100vh",
        font_family="Futura",
    )
