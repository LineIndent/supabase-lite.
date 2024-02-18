import reflex as rx


def render_attribute():
    return rx.hstack(
        rx.text("Built with", font_weight="bold", font_size="14px", opacity="0.91"),
        rx.image(
            src="reflex.svg",
            filter="invert(100%)",
            html_height="72px",
            html_width="72px",
        ),
        width="100%",
        padding="1rem",
        display="flex",
        justify_content="center",
        align_items="center",
        bg="#171a21",
    )
