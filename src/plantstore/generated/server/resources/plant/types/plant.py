# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .plant_category import PlantCategory
from .plant_id import PlantId
from .plant_status import PlantStatus


class Plant(pydantic.BaseModel):
    id: typing.Optional[PlantId]
    category: typing.Optional[PlantCategory]
    name: str
    photo_urls: typing.Dict[str, str] = pydantic.Field(alias="photoUrls")
    status: typing.Optional[PlantStatus]

    class Partial(typing_extensions.TypedDict):
        id: typing_extensions.NotRequired[typing.Optional[PlantId]]
        category: typing_extensions.NotRequired[typing.Optional[PlantCategory]]
        name: typing_extensions.NotRequired[str]
        photo_urls: typing_extensions.NotRequired[typing.Dict[str, str]]
        status: typing_extensions.NotRequired[typing.Optional[PlantStatus]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
