import reflex as rx
from ..states.table import TableState


def create_table_header(title: str):
    return rx.table.column_header_cell(title)


def create_query_rows(data: dict[str, str]):
    def fill_rows_with_data(data_):
        return rx.table.cell(
            data_[1],
            cursor="pointer",
        )

    return rx.table.row(
        rx.foreach(data, fill_rows_with_data),
        _hover={"bg": rx.color(color="gray", shade=4)},
    )


def create_pagination():
    return rx.hstack(
        rx.hstack(
            rx.text("Entries per page", weight="bold"),
            rx.select(
                TableState.limits, default_value="10", on_change=TableState.delta_limit
            ),
            align_items="center",
        ),
        rx.hstack(
            rx.text(
                f"Page { TableState.current_page }/{ TableState.total_pages }",
                width="100px",
                weight="bold",
            ),
            rx.chakra.button_group(
                rx.icon(
                    tag="chevron-left", on_click=TableState.previous, cursor="pointer"
                ),
                rx.icon(
                    tag="chevron-right", on_click=TableState.next, cursor="pointer"
                ),
                is_attached=True,
            ),
            align_items="center",
            spacing="1",
        ),
        align_items="center",
        spacing="4",
    )


def render_output():
    return rx.center(
        rx.vstack(
            create_pagination(),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.foreach(TableState.column_names, create_table_header)
                    ),
                ),
                rx.table.body(rx.foreach(TableState.paginated_data, create_query_rows)),
                width="100%",
                variant="surface",
                size="1",
            ),
            width="100%",
            overflow="auto",
            padding="2em 2em",
        ),
        width="100%",
        border_radius="10px",
        overflow="auto",
    )
