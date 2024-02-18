import reflex as rx

from rx_client.states import State, Status

STATUS = {
    "text": {
        "font_size": "10px",
        "font_color": "#404040",
        "font_weight": "bold",
    },
    "stack": {
        "transition": "all 550ms ease 3s",
        "display": "flex",
        "justify_content": "center",
        "align_items": "center",
    },
}


def render_supabase_status():
    """Supabase API status.

    Returns:
        rx.badge: The UI component for status info.
    """
    return rx.hstack(
        rx.text("SUPABASE", style=STATUS.get("text")),
        rx.badge(
            State.supabase_status,
            color_scheme=State.supabase_status_color,
            size="1",
            variant="outline",
        ),
        opacity=Status.s_opacity,
        style=STATUS.get("stack"),
    )


def render_reflex_status():
    """Reflex API status.

    Returns:
        rx.badge: The UI component for status info.
    """
    return rx.hstack(
        rx.text("REFLEX", style=STATUS.get("text")),
        rx.badge(
            State.reflex_status,
            color_scheme=State.reflex_status_color,
            size="1",
            variant="outline",
        ),
        opacity=Status.r_opacity,
        style=STATUS.get("stack"),
    )
