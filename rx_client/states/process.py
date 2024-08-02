from .base import Base
import reflex as rx
import httpx
import json


class Process(Base):
    async def toggle_method_selection(self, method: str):
        self.selected_method = method.lower()

    async def process_headers(self):
        header = {
            x.key: x.value for x in self.headers if x.key != "id" or x.key != "type"
        }

        return header

    async def run_request(self):
        if self.selected_method:
            self.output = ""
            self.is_table = False
            client = getattr(self, self.selected_method)
            await client()

    async def auth(self, url: str, data: dict[str, str] = None):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/{url}", headers=await self.auth_headers(), json=data
            )

        return response

    async def rest(self, table: str, column: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/rest/v1/{table}?select={column}",
                headers=await self.process_headers(),
            )

        return response

    async def signup(self):
        data = {}
        await self.auth("auth/v1/signup", data)

    async def login(self):
        data = {}
        await self.auth("auth/v1/token?grant_type=password", data)

    async def logout(self):
        await self.auth("auth/v1/logout")

    async def get(self):
        if not self.table or not self.column:
            return await self.error_callback("Incomplete form!")

        response = await self.rest(self.table, self.column)
        self.output = json.dumps(response.json(), indent=4, sort_keys=True)

        await self.process_table(response.json())

    async def post(self): ...

    async def delete(self): ...

    async def process_table(self, data: list[dict[str, str]]):
        self.main_data = data
        self.number_of_rows = len(data)
        self.column_names = list(data[0].keys()) if data else []

        self.is_table = True

    async def error_callback(self, msg: str):
        return rx.toast.error(msg)
