import reflex as rx

from rx_client.states import RequestAPI


BOX = {
    "height": "60vh",
    "border": "1px solid #31353b",
    "border_radius": "10px",
    "bg": "none",
    "spacing": "0",
    "flex": ["100%", "100%", "100%", "65%", "65%"],
    "overflow": "hidden",
    "box_header": {
        "width": "100%",
        "padding": "1em 1em",
        "border_bottom": "1px solid #31353b",
        "background_color": rx.color_mode_cond(
            "none",
            "#171a21",
        ),
    },
}


box_name = rx.badge(
    "Request Output",
    color_scheme="grass",
    size="1",
)


def render_output_box():
    """_summary_

    Returns:
        _type_: _description_
    """

    return rx.vstack(
        rx.hstack(
            rx.spacer(),
            box_name,
            style=BOX.get("box_header"),
        ),
        rx.match(
            RequestAPI.output,
            (
                "",
                rx.center(
                    rx.text("No Output.", font_weight="bold", font_size="12px"),
                    width="100%",
                    height="inherit",
                ),
            ),
            rx.code_block(
                RequestAPI.output,
                language="json",
                width="100%",
                min_height="inherit",
                wrap_long_lines=True,
                custom_style={"background_color": "transparent"},
                code_tag_props={"pre": {"background_color": "transparent"}},
            ),
        ),
        style=BOX,
    )
