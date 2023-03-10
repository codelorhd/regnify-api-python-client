# coding: utf-8

"""
    REGNIFY HTTP API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: admin@regnify.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from regnify import schemas  # noqa: F401


class UserCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "password",
            "last_name",
            "first_name",
            "email",
        }
        
        class properties:
            email = schemas.StrSchema
            
            
            class last_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class first_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            password = schemas.StrSchema
            access_begin = schemas.DateTimeSchema
            access_end = schemas.DateTimeSchema
            is_super_admin = schemas.BoolSchema
            __annotations__ = {
                "email": email,
                "last_name": last_name,
                "first_name": first_name,
                "password": password,
                "access_begin": access_begin,
                "access_end": access_end,
                "is_super_admin": is_super_admin,
            }
    
    password: MetaOapg.properties.password
    last_name: MetaOapg.properties.last_name
    first_name: MetaOapg.properties.first_name
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_begin"]) -> MetaOapg.properties.access_begin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_end"]) -> MetaOapg.properties.access_end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_super_admin"]) -> MetaOapg.properties.is_super_admin: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "last_name", "first_name", "password", "access_begin", "access_end", "is_super_admin", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_begin"]) -> typing.Union[MetaOapg.properties.access_begin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_end"]) -> typing.Union[MetaOapg.properties.access_end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_super_admin"]) -> typing.Union[MetaOapg.properties.is_super_admin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "last_name", "first_name", "password", "access_begin", "access_end", "is_super_admin", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        last_name: typing.Union[MetaOapg.properties.last_name, str, ],
        first_name: typing.Union[MetaOapg.properties.first_name, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        access_begin: typing.Union[MetaOapg.properties.access_begin, str, datetime, schemas.Unset] = schemas.unset,
        access_end: typing.Union[MetaOapg.properties.access_end, str, datetime, schemas.Unset] = schemas.unset,
        is_super_admin: typing.Union[MetaOapg.properties.is_super_admin, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserCreate':
        return super().__new__(
            cls,
            *_args,
            password=password,
            last_name=last_name,
            first_name=first_name,
            email=email,
            access_begin=access_begin,
            access_end=access_end,
            is_super_admin=is_super_admin,
            _configuration=_configuration,
            **kwargs,
        )
