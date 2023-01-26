# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions

from .plant_id import PlantId


class InvalidId(pydantic.BaseModel):
    id: PlantId
    message: str

    class Partial(typing_extensions.TypedDict):
        id: typing_extensions.NotRequired[PlantId]
        message: typing_extensions.NotRequired[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
