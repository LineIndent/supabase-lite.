import reflex as rx

navbar: dict[str, str] = {
    "width": "100%",
    "padding": "24px",
    "justify_content": "space-between",
    # "position": "sticky",
    # "top": "0",
    "align_items": "center",
    "z_index": "99",
    "background": "#161718",
}

inner: dict[str, str] = {
    "display": "flex",
    "align_items": "center",
}

text: dict[str, str] = {
    "font_family": "var(--chakra-fonts-branding)",
    "font_weight": "var(--chakra-fontWeights-black)",
}


def render_navbar():
    return rx.hstack(
        # left side header ...
        rx.hstack(
            rx.chakra.text(
                "supabase-lite.", font_size="var(--chakra-fontSizes-2xl)", **text
            ),
            **inner,
        ),
        # right side header ...
        rx.hstack(),
        **navbar,
    )
