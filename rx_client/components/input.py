import reflex as rx

from rx_client.components.entry import render_text_entry, render_key_value_entries
from rx_client.states import (
    AddObject,
    RequestAPI,
    ResetObject,
    State,
    Update,
    WebObject,
)

BOX = {
    "overflow": "hidden",
    "flex": ["100%", "100%", "100%", "30%", "30%"],
    "entry_ui": {
        "border_bottom": "1px solid #373a3e",
        "width": "100%",
        "title": {"font_size": "12px"},
    },
    "key_value_stack": {
        "width": "100%",
        "border_top": "1px solid red",
        "border_bottom": "1px solid #404040",
        "padding_left": ["1rem", "1rem", "1rem", "3rem", "3rem"],
    },
    "key_value_type": {"opacity": "0.61", "width": "60px", "font_size": "12px"},
    "web_object": {
        "width": "100%",
        "border_bottom": "1px solid #373a3e",
        "padding": "1em 0em",
        "display": "flex",
        "align_items": "center",
        "justify_content": "space-between",
    },
    "vstack_web_object": {
        "display": "flex",
        "align_items": "center",
        "width": "100%",
        "padding_left": "0.5em",
    },
    "tags": {
        "width": "100%",
        "display": "flex",
        "flex_wrap": "wrap",
        "justify_content": "start",
        "align_items": "start",
        "gap": "0.65em 0.45em",
        "padding_top": "0.35em",
        "padding_bottom": "0.85em",
    },
}


def create_entry_ui(title: str, component: rx.Component):
    return rx.vstack(
        rx.text(title, style=BOX.get("entry_ui").get("title")),
        component,
        style=BOX.get("entry_ui"),
        spacing="0",
    )


def create_key_value_entry_ui(object: WebObject):
    return rx.hstack(
        rx.text(f"-{object.type}", style=BOX.get("key_value_type")),
        *render_key_value_entries(
            object,
            lambda e: Update.key(e, object),
            lambda e: Update.value(e, object),
        ),
        style=BOX.get("vstack_web_object"),
    )


def create_web_object_ui(title: str, _type_: str):
    return rx.hstack(
        rx.text(
            title,
            style=BOX.get("entry_ui").get("title"),
        ),
        rx.spacer(),
        rx.badge(
            _type_,
            cursor="pointer",
            on_click=AddObject.add(_type_),
            color_scheme="grass",
            size="1",
        ),
        rx.badge(
            "R",
            cursor="pointer",
            size="1",
            color_scheme="ruby",
            on_click=ResetObject.reset_list(_type_),
        ),
        style=BOX.get("web_object"),
    )


def render_tag_badge(tag: list[str]):
    return rx.badge(
        tag[0],
        variant="surface",
        color_scheme=tag[1],
        on_click=Update.update_tag(tag),
        cursor="pointer",
        transition="all 450ms ease",
        size="1",
    )


def render_input_box():
    """_summary_

    Returns:
        _type_: _description_
    """

    return rx.vstack(
        create_entry_ui(
            "Supabase API Key",
            rx.box(
                render_text_entry(
                    State.api_key,
                    "Supabase API Key",
                    State.set_api_key,
                ),
                width="100%",
            ),
        ),
        create_entry_ui(
            "Supabase Project URL",
            rx.box(
                render_text_entry(
                    State.project_url,
                    "Supabase Project URL",
                    State.set_project_url,
                ),
                width="100%",
            ),
        ),
        create_entry_ui(
            "Node Name",
            rx.box(
                render_text_entry(
                    State.node,
                    "Supabase API Key",
                    State.set_node,
                ),
                width="100%",
            ),
        ),
        # method tags ...
        rx.vstack(
            rx.text("Select Method", style=BOX.get("entry_ui").get("title")),
            rx.hstack(
                rx.foreach(State.method_tags, render_tag_badge),
                spacing="3",
                style=BOX.get("tags"),
            ),
            border_bottom="1px solid #373a3e",
            spacing="1",
            width="100%",
        ),
        rx.vstack(
            create_web_object_ui("Header", "H"),
            rx.foreach(
                State.headers,
                create_key_value_entry_ui,
            ),
            width="100%",
        ),
        rx.vstack(
            create_web_object_ui("Data", "D"),
            rx.foreach(
                State.datas,
                create_key_value_entry_ui,
            ),
            width="100%",
        ),
        rx.vstack(
            create_web_object_ui("Specific", "S"),
            rx.foreach(
                State.specific,
                create_key_value_entry_ui,
            ),
            width="100%",
        ),
        rx.hstack(
            rx.badge(
                rx.text(
                    "Send Request",
                    text_align="center",
                    width="100%",
                ),
                color_scheme="grass",
                variant="surface",
                size="2",
                radius="none",
                padding="1em",
                cursor="pointer",
                on_click=RequestAPI.start_request_process,
                width="100%",
            ),
            width="100%",
            padding_top="1.25em",
        ),
        spacing="5",
        style=BOX,
    )
