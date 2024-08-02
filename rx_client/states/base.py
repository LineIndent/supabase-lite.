import reflex as rx


class WebObject(rx.Base):
    id: int
    type: str  # H=header; D=data; S=specific
    key: str
    value: str


class Base(rx.State):
    #
    base_url: str
    anon_key: str
    table: str
    column: str

    #
    method_list: list[str] = [
        "GET",
        "POST",
        "DELETE",
        "LOGIN",
        "SIGNUP",
        "LOGOUT",
    ]
    selected_method: str

    #
    headers: list[WebObject]
    datas: list[WebObject]
    output: str

    #
    is_table: bool = False
    main_data: list[dict[str, str]]
    number_of_rows: int = 10
    column_names: list[str]

    current_limit: int = 10
    limits: list[str] = ["10", "20", "50"]
    offset: int = 0
    current_page: int = 1
    total_pages: int = (number_of_rows + current_limit - 1) // current_limit
    paginated_data: list[dict[str, str]]
