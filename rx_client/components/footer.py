import reflex as rx
from rx_client.components.attribute import render_attribute
from rx_client.components.socials import render_socials

GET = """
### Request GET (operational) <span style="display:inline-flex; align-items: center; vertical-align: middle; width: 10px; height: 10px; background-color: green; border-radius: 50%;"></span>
#### H **apikey**: SUPABASE_KEY
#### H **Authorization**: Bearer ACCESS_TOKEN
"""

POST = """
### Request POST (operational) <span style="display:inline-flex; align-items: center; vertical-align: middle; width: 10px; height: 10px; background-color: green; border-radius: 50%;"></span>
#### H **apikey**: SUPABASE_KEY
#### H **Authorization**: Bearer ACCESS_TOKEN
#### H **Content-Type**: application/json
#### d { '**column_name**': 'some_value', '**other_column_name**': 'other_value' }
"""

DELETE = """
### Request DELETE (operational) <span style="display:inline-flex; align-items: center; vertical-align: middle; width: 10px; height: 10px; background-color: green; border-radius: 50%;"></span>
#### H **apikey**: SUPABASE_KEY
#### H **Authorization**: Bearer ACCESS_TOKEN
#### S { '**column_name**': 'some_value' }
"""

PATCH = """
### Request PATCH (in progress) <span style="display:inline-flex; align-items: center; vertical-align: middle; width: 10px; height: 10px; background-color: orange; border-radius: 50%;"></span>
#### H **apikey**: SUPABASE_KEY 
#### H **Authorization**: Bearer ACCESS_TOKEN
#### H **Content-Type**: application/json
#### d { '**column_name**': 'some_value' }
"""

LOGOUT = """
### Request LOGOUT (operational) <span style="display:inline-flex; align-items: center; vertical-align: middle; width: 10px; height: 10px; background-color: green; border-radius: 50%;"></span>
#### H **apikey**: SUPABASE_KEY
#### H **Authorization**: Bearer ACCESS_TOKEN
#### H **Content-Type**: application/json 
"""

LOGIN = """
### Request LOGIN (operational) <span style="display:inline-flex; align-items: center; vertical-align: middle; width: 10px; height: 10px; background-color: green; border-radius: 50%;"></span>
#### H **apikey**: SUPABASE_KEY
#### H **Content-Type**: application/json
#### d {'email': 'someone@email.com', 'password': 'qDdkSkhAEvJQAHZNxsmF'}
"""

SIGNUP = """
### Request SIGNUP (in progress) <span style="display:inline-flex; align-items: center; vertical-align: middle; width: 10px; height: 10px; background-color: orange; border-radius: 50%;"></span>
#### H **apikey**: SUPABASE_KEY
#### H **Content-Type**: application/json
#### d {'email': 'someone@email.com', 'password': 'qDdkSkhAEvJQAHZNxsmF'}
"""


__map__ = {
    "h3": lambda text: rx.chakra.text(text, font_size="13px", margin_y="0.75em"),
    "h4": lambda text: rx.chakra.text(text, font_size="11px", opacity="0.91"),
}


def create_footer_item(title: str):
    return rx.box(
        rx.markdown(
            title,
            component_map=__map__,
        ),
        flex=["100%", "100%", "50%", "25%", "25%"],
    )


FOOTER = {
    "width": "100%",
    "display": "flex",
    "flex_wrap": "wrap",
    "justify_content": "space-between",
    "align_items": "start",
    "gap": "1em 0.4em",
}

SOCIALS = [["github.svg", "https://github.com/LineIndent"]]


def render_footer():
    return rx.vstack(
        rx.text(
            "API Endpoint Notations",
            font_weight="bolder",
            padding=["0em 2em", "0em 2em", "0em 2em", "0em 5em", "0em 5em"],
        ),
        rx.hstack(
            create_footer_item(SIGNUP),
            create_footer_item(POST),
            create_footer_item(DELETE),
            create_footer_item(PATCH),
            create_footer_item(LOGOUT),
            create_footer_item(LOGIN),
            create_footer_item(GET),
            padding=["1em 2em", "1em 2em", "1em 2em", "1em 5em", "1em 5em"],
            style=FOOTER,
        ),
        *[rx.spacer() for _ in range(4)],
        render_socials("Social Media", SOCIALS),
        render_attribute(),
        width="100%",
        border="1px solid #404040",
        padding="4em 0em 0em 0em",
    )
