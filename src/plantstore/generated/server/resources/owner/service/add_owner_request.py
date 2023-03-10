# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ...plant.types.plant import Plant
from ..types.owner_age import OwnerAge


class AddOwnerRequest(pydantic.BaseModel):
    name: str
    age: OwnerAge
    plants: typing.List[Plant]

    class Partial(typing_extensions.TypedDict):
        name: typing_extensions.NotRequired[str]
        age: typing_extensions.NotRequired[OwnerAge]
        plants: typing_extensions.NotRequired[typing.List[Plant]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
