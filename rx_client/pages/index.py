import reflex as rx
from rx_client.components.landing import render_landing
from rx_client.components.header import render_header
from rx_client.components.footer import render_footer
from rx_client.components.title import render_title
from rx_client.components.status import render_supabase_status, render_reflex_status
from rx_client.components.output import render_output_box
from rx_client.components.input import render_input_box

from rx_client.states import Status


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
        "padding": ["2em 2em", "2em 2em", "2em 4em", "2em 4em", "2em 4em"],
    },
}


@rx.page("/", on_load=[Status.get_supabase_status, Status.get_reflex_status])
def client() -> rx.Component:
    """The client page.
    Returns:
        The UI for the client page.
    """

    return rx.vstack(
        render_header(),
        render_landing(),
        rx.hstack(
            render_title(),
            rx.hstack(render_supabase_status(), render_reflex_status(), spacing="5"),
            style=CLIENT.get("title_and_status"),
        ),
        rx.box(
            rx.divider(size="3", width="100%"),
            padding=["0em 2em", "0em 2em", "0em 4em", "0em 4em", "0em 4em"],
            width="100%",
        ),
        rx.hstack(
            render_output_box(),
            render_input_box(),
            spacing="6",
            style=CLIENT.get("data_boxes"),
        ),
        render_footer(),
        style=CLIENT,
    )
