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


class ManySystemScopeOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "scopes",
        }
        
        class properties:
            
            
            class scopes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SystemScopeOut']:
                        return SystemScopeOut
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SystemScopeOut'], typing.List['SystemScopeOut']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'scopes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SystemScopeOut':
                    return super().__getitem__(i)
            __annotations__ = {
                "scopes": scopes,
            }
    
    scopes: MetaOapg.properties.scopes
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scopes"]) -> MetaOapg.properties.scopes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["scopes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scopes"]) -> MetaOapg.properties.scopes: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["scopes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        scopes: typing.Union[MetaOapg.properties.scopes, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManySystemScopeOut':
        return super().__new__(
            cls,
            *_args,
            scopes=scopes,
            _configuration=_configuration,
            **kwargs,
        )

from regnify.model.system_scope_out import SystemScopeOut
