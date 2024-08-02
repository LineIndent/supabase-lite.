import reflex as rx

from ..states.base import Base
from ..components.table import render_output

BOX = {
    "height": "90vh",
    "border_radius": "8px",
    "spacing": "0",
    "flex": ["100%", "100%", "100%", "65%", "65%"],
    "overflow": "hidden",
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
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Output", value="1"),
                rx.tabs.trigger("Table", value="2"),
                justify_content="end",
            ),
            rx.tabs.content(
                rx.match(
                    Base.output,
                    (
                        "",
                        rx.center(
                            rx.text("No Output.", font_weight="bold", font_size="14px"),
                            width="100%",
                            height="90vh",
                        ),
                    ),
                    rx.code_block(
                        Base.output,
                        language="json",
                        width="100%",
                        min_height="inherit",
                        wrap_long_lines=True,
                        custom_style={"background_color": "transparent"},
                        code_tag_props={"pre": {"background_color": "transparent"}},
                        overflow="auto",
                    ),
                ),
                value="1",
                bg="rgba(17, 19, 18, 0.5)",
                margin="15px 0px",
                border_radius="8px",
                height="90vh",
            ),
            rx.tabs.content(
                rx.cond(
                    Base.is_table,
                    render_output(),
                    rx.center(
                        rx.text("No Data Table.", font_weight="bold", font_size="14px"),
                        width="100%",
                        height="90vh",
                    ),
                ),
                value="2",
                bg="rgba(17, 19, 18, 0.5)",
                margin="15px 0px",
                border_radius="8px",
                height="90vh",
            ),
            width="100%",
            height="90vh",
            default_value="1",
            transition="all 400ms ease",
            padding="10px",
        ),
        style=BOX,
    )
