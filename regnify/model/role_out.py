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


class RoleOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "date_created",
            "permissions",
            "can_be_deleted",
            "id",
            "title",
            "created_by_user",
        }
        
        class properties:
            id = schemas.UUIDSchema
            title = schemas.StrSchema
            
            
            class permissions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'permissions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            can_be_deleted = schemas.BoolSchema
        
            @staticmethod
            def created_by_user() -> typing.Type['UserOut']:
                return UserOut
            date_created = schemas.DateTimeSchema
        
            @staticmethod
            def modified_by_user() -> typing.Type['UserOut']:
                return UserOut
            date_modified = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "title": title,
                "permissions": permissions,
                "can_be_deleted": can_be_deleted,
                "created_by_user": created_by_user,
                "date_created": date_created,
                "modified_by_user": modified_by_user,
                "date_modified": date_modified,
            }
    
    date_created: MetaOapg.properties.date_created
    permissions: MetaOapg.properties.permissions
    can_be_deleted: MetaOapg.properties.can_be_deleted
    id: MetaOapg.properties.id
    title: MetaOapg.properties.title
    created_by_user: 'UserOut'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_be_deleted"]) -> MetaOapg.properties.can_be_deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by_user"]) -> 'UserOut': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified_by_user"]) -> 'UserOut': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_modified"]) -> MetaOapg.properties.date_modified: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "title", "permissions", "can_be_deleted", "created_by_user", "date_created", "modified_by_user", "date_modified", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_be_deleted"]) -> MetaOapg.properties.can_be_deleted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by_user"]) -> 'UserOut': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified_by_user"]) -> typing.Union['UserOut', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_modified"]) -> typing.Union[MetaOapg.properties.date_modified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "title", "permissions", "can_be_deleted", "created_by_user", "date_created", "modified_by_user", "date_modified", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        date_created: typing.Union[MetaOapg.properties.date_created, str, datetime, ],
        permissions: typing.Union[MetaOapg.properties.permissions, list, tuple, ],
        can_be_deleted: typing.Union[MetaOapg.properties.can_be_deleted, bool, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        created_by_user: 'UserOut',
        modified_by_user: typing.Union['UserOut', schemas.Unset] = schemas.unset,
        date_modified: typing.Union[MetaOapg.properties.date_modified, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RoleOut':
        return super().__new__(
            cls,
            *_args,
            date_created=date_created,
            permissions=permissions,
            can_be_deleted=can_be_deleted,
            id=id,
            title=title,
            created_by_user=created_by_user,
            modified_by_user=modified_by_user,
            date_modified=date_modified,
            _configuration=_configuration,
            **kwargs,
        )

from regnify.model.user_out import UserOut