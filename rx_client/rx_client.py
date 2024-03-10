#  API Client Web Application for Supabase Endpoint Testing.
#  Feb. 18, 2024 - S. Ahmad P. Hakimi

import reflex as rx
from rx_client.pages import *


APP = {
    "_light": {"bg": "#f0fff0"},
    "_dark": {"bg": "#1a1a1a"},
}

app = rx.App(style=APP, theme=rx.theme(appearance="dark"))
