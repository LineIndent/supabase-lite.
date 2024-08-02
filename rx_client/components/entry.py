import reflex as rx
from ..states.base import WebObject


def render_text_entry(value: str, placeholder: str, update: rx.State):
    return rx.chakra.input(
        value=value,
        placeholder=placeholder,
        on_change=update,
        height="32px",
        outline="none",
        variant="unstyled",
    )


def render_key_value_entries(
    item: WebObject, _key_update: rx.State, _value_update: rx.State
):
    return [
        rx.input(value=item.key, on_change=_key_update, placeholder="Key"),
        rx.input(value=item.value, on_change=_value_update, placeholder="Value"),
    ]
