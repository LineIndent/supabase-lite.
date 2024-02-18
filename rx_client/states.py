import json
import reflex as rx
import httpx


class WebObject(rx.Base):
    id: int
    type: str  # H=header; D=data; S=specific
    key: str
    value: str


class State(rx.State):
    api_key: str
    project_url: str
    node: str
    method: str

    headers: list[WebObject]
    datas: list[WebObject]
    specific: list[WebObject]

    supabase_status: str
    supabase_status_color: str

    reflex_status: str
    reflex_status_color: str


class Status(State):

    s_opacity: str = "0"
    r_opacity: str = "0"

    async def get_supabase_status(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://status.supabase.com")

            if response.status_code == 200:
                self.supabase_status = "OK"
                self.supabase_status_color = "grass"

            else:
                self.supabase_status = "Status: Error."
                self.supabase_status_color = "orange"

            self.s_opacity = "1"

    async def get_reflex_status(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://status.supabase.com")

            if response.status_code == 200:
                self.reflex_status = "OK"
                self.reflex_status_color = "grass"

            else:
                self.reflex_status = "Status: Error."
                self.reflex_status_color = "orange"

            self.r_opacity = "1"


class ResetObject(State):

    async def reset_list(self, _type_):
        if _type_ == "H":
            self.headers = []
        if _type_ == "D":
            self.datas = []
        if _type_ == "S":
            self.specific = []


class AddObject(State):

    h_counter: int = 0
    d_counter: int = 0
    s_counter: int = 0

    async def create_web_object(self, _type_):
        return WebObject(
            id=(self.h_counter if _type_ == "H" else self.d_counter),
            type=_type_,
            key="",
            value="",
        )

    async def add(self, _type_: str):
        obj = await self.create_web_object(_type_)

        if _type_ == "H":
            self.headers.append(obj)
        elif _type_ == "D":
            self.datas.append(obj)
        else:
            self.specific.append(obj)

        if _type_ == "H":
            self.h_counter += 1

        if _type_ == "D":
            self.d_counter += 1

        if _type_ == "S":
            self.s_counter += 1


class Update(State):

    async def type_header(self, _object, object):
        self.headers = [
            _object if header.id == object["id"] else header for header in self.headers
        ]

    async def type_data(self, _object, object):
        self.datas = [
            _object if header.id == object["id"] else header for header in self.datas
        ]

    async def type_specific(self, _object, object):
        self.specific = [
            _object if header.id == object["id"] else header for header in self.specific
        ]

    async def update_list(self, _object, object):
        if object["type"] == "H":
            await self.type_header(_object, object)
        elif object["type"] == "D":
            await self.type_data(_object, object)
        else:
            await self.type_specific(_object, object)

    async def key(self, value, object: dict):
        _object = WebObject(
            id=object["id"],
            type=object["type"],
            key=value,
            value=object["value"],
        )

        await self.update_list(_object, object)

    async def value(self, value, object: dict):
        _object = WebObject(
            id=object["id"],
            type=object["type"],
            key=object["key"],
            value=value,
        )

        await self.update_list(_object, object)


class RequestAPI(State):

    url: str
    output: str

    async def start_request_process(self):
        client = getattr(self, self.method.lower())

        await client()

    async def send_request(self):
        async with httpx.AsyncClient() as client:
            _client = getattr(client, self.method.lower())

            if self.method in ("GET", "DELETE"):
                response = await _client(
                    self.url, headers={x.key: x.value for x in self.headers}
                )

                if self.moth == "GET":
                    self.output = json.dumps(response.json(), indent=4, sort_keys=True)

            if self.method in ("POST"):
                try:
                    response = await _client(
                        self.url,
                        headers={x.key: x.value for x in self.headers},
                        json={x.key: x.value for x in self.datas},
                    )

                    self.output = json.dumps(response.json(), indent=4, sort_keys=True)

                except Exception as error:
                    print(error)

    async def login(self):
        """
        User login.

        Required headers and/or data
            -H "apikey: SUPABASE_KEY" [DEFAULT SET]
            -H "Content-Type: application/json"
            -d {"email": "someone@email.com", "password": "qDdkSkhAEvJQAHZNxsmF"}

        """
        self.url += self.project_url + "/auth/v1/token?grant_type=password"
        self.method = "POST"

        await self.send_request()

    async def get(self):
        """
        GET request for given node name (node name = tabel name, etc ...).

        Use to SELECT data from DATABASE.

        Required headers and/or data:
            -H "apikey: SUPABASE_KEY"
            -H "Authorization: Bearer ACCESS_TOKEN"

        """
        self.url, self.method = (
            self.project_url + "/rest/v1/" + self.node,
            "GET",
        )

        await self.send_request()

    async def post(self):
        """
        POST request for given node name (node name = tabel name, etc ...).

        Use to INSERT data into DATABASE.

        Required headers and/or data:
            -H "apikey: SUPABASE_KEY" [DEFAULT SET]
            -H "Authorization: Bearer ACCESS_TOKEN"
            -H "Content-Type: application/json"
            -H "Prefer: return=minimal" [OPTIONAL]
            -d { "column_name": "some_value", "other_column_name": "other_value" }

        """
        self.url, self.method = (
            self.project_url + "/rest/v1/" + self.node,
            "POST",
        )

        await self.send_request()

    async def delete(self):
        """
        DELETE request for a given node name (node name = tabel name, etc ...).

        Use to DELETE data into DATABASE.
        If column and value are given, matches specific row.

        The specific() method could also be used to pass in column/value.

        Required headers and/or data:
            -H "apikey: SUPABASE_KEY" [DEFAULT SET]
            -H "Authorization: Bearer SUPABASE_KEY"
            -S {'column)name': 'column_value'}
        """

        string = self.project_url + "/rest/v1/" + self.node

        for object in self.specific:
            self.url = string + "?" + object.key + "=eq." + object.value

        self.method = "DELETE"

        await self.send_request()
