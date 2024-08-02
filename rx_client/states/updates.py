from .base import Base, WebObject


class ResetObject(Base):

    async def reset_list(self, _type_):
        if _type_ == "H":
            self.headers = []
        if _type_ == "D":
            self.datas = []
        if _type_ == "S":
            self.specific = []


class AddObject(Base):

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


class Update(Base):

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
