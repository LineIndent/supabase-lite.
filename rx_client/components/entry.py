import reflex as rx
from rx_client.states import WebObject


def render_text_entry(value: str, placeholder: str, update: rx.State):
    return rx.input(
        value=value,
        placeholder=placeholder,
        on_change=update,
        variant=rx.Var.create("none"),
        padding="1em 0em",
        outline="none",
    )


def render_key_value_entries(
    item: WebObject, _key_update: rx.State, _value_update: rx.State
):
    return [
        rx.input(value=item.key, on_change=_key_update, placeholder="Key"),
        rx.input(value=item.value, on_change=_value_update, placeholder="Value"),
    ]
