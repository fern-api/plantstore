# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .category_id import CategoryId


class PlantCategory(pydantic.BaseModel):
    id: CategoryId
    name: str

    class Partial(typing_extensions.TypedDict):
        id: typing_extensions.NotRequired[CategoryId]
        name: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @PlantCategory.Validators.root()
            def validate(values: PlantCategory.Partial) -> PlantCategory.Partial:
                ...

            @PlantCategory.Validators.field("id")
            def validate_id(id: CategoryId, values: PlantCategory.Partial) -> CategoryId:
                ...

            @PlantCategory.Validators.field("name")
            def validate_name(name: str, values: PlantCategory.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[PlantCategory.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[PlantCategory.Validators._RootValidator]] = []
        _id_pre_validators: typing.ClassVar[typing.List[PlantCategory.Validators.PreIdValidator]] = []
        _id_post_validators: typing.ClassVar[typing.List[PlantCategory.Validators.IdValidator]] = []
        _name_pre_validators: typing.ClassVar[typing.List[PlantCategory.Validators.PreNameValidator]] = []
        _name_post_validators: typing.ClassVar[typing.List[PlantCategory.Validators.NameValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[PlantCategory.Validators._RootValidator], PlantCategory.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[PlantCategory.Validators._PreRootValidator], PlantCategory.Validators._PreRootValidator]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[PlantCategory.Validators.PreIdValidator], PlantCategory.Validators.PreIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[PlantCategory.Validators.IdValidator], PlantCategory.Validators.IdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[PlantCategory.Validators.PreNameValidator], PlantCategory.Validators.PreNameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[PlantCategory.Validators.NameValidator], PlantCategory.Validators.NameValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "id":
                    if pre:
                        cls._id_pre_validators.append(validator)
                    else:
                        cls._id_post_validators.append(validator)
                if field_name == "name":
                    if pre:
                        cls._name_pre_validators.append(validator)
                    else:
                        cls._name_post_validators.append(validator)
                return validator

            return decorator

        class PreIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: PlantCategory.Partial) -> typing.Any:
                ...

        class IdValidator(typing_extensions.Protocol):
            def __call__(self, __v: CategoryId, __values: PlantCategory.Partial) -> CategoryId:
                ...

        class PreNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: PlantCategory.Partial) -> typing.Any:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: PlantCategory.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: PlantCategory.Partial) -> PlantCategory.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: PlantCategory.Partial) -> PlantCategory.Partial:
        for validator in PlantCategory.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: PlantCategory.Partial) -> PlantCategory.Partial:
        for validator in PlantCategory.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("id", pre=True)
    def _pre_validate_id(cls, v: CategoryId, values: PlantCategory.Partial) -> CategoryId:
        for validator in PlantCategory.Validators._id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("id", pre=False)
    def _post_validate_id(cls, v: CategoryId, values: PlantCategory.Partial) -> CategoryId:
        for validator in PlantCategory.Validators._id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=True)
    def _pre_validate_name(cls, v: str, values: PlantCategory.Partial) -> str:
        for validator in PlantCategory.Validators._name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=False)
    def _post_validate_name(cls, v: str, values: PlantCategory.Partial) -> str:
        for validator in PlantCategory.Validators._name_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
