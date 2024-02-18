import reflex as rx

TEXT = {
    "font_size": ["2.25em", "2.6em", "2.75em", "3.5em", "4em"],
    "font_weight": "900",
    "letter_spacing": "0.15rem",
    "transition": "all 400ms ease",
    "text_align": "center",
    "background_clip": "text",
    "stack": {
        "width": "100%",
        "height": "105vh",
        "display": "flex",
        "justify_content": "start",
        "align_items": "center",
        "padding": ["3em 2em", "4em 2em", "4em 4em", "6em 4em", "8em 4em"],
    },
}

ARROW: dict = {
    "@keyframes arrow": {
        "0%": {"transform": "scale(1.15)"},
        "100%": {"transform": "scale(0.85)"},
    },
    "animation": "arrow 750ms cubic-bezier(0.250, 0.460, 0.450, 0.940) infinite alternate-reverse both",
}

OPAC = {
    "position": "relative",
    f"@keyframes opacity": {
        "0%": {"opacity": "0"},
        "100%": {"opacity": "1"},
    },
    "animation": "opacity 3s ease",
}


def render_landing():
    return rx.vstack(
        rx.vstack(
            rx.chakra.heading("Supabase API Client", style=TEXT),
            rx.chakra.heading("Lightweight. Minimal. Simple.", style=TEXT),
            bg="linear-gradient(315deg, rgb(66, 211, 146) 25%, rgb(100, 126, 255))",
            background_clip="text",
            display="flex",
            align_items="center",
            style=OPAC,
        ),
        rx.spacer(),
        rx.box(
            rx.link(rx.icon(tag="chevron_down"), href="#client"),
            display="flex",
            justify_content="center",
            align_items="center",
            border_radius="50%",
            border="1px solid #fff",
            padding="0.5em 0.5em",
            style=ARROW,
        ),
        style=TEXT.get("stack"),
    )
