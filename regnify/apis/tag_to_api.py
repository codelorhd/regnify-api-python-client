import typing_extensions

from regnify.apis.tags import TagValues
from regnify.apis.tags.auth_api import AuthApi
from regnify.apis.tags.roles_and_permissions_api import RolesAndPermissionsApi
from regnify.apis.tags.users_api import UsersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTH: AuthApi,
        TagValues.ROLES_AND_PERMISSIONS: RolesAndPermissionsApi,
        TagValues.USERS: UsersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTH: AuthApi,
        TagValues.ROLES_AND_PERMISSIONS: RolesAndPermissionsApi,
        TagValues.USERS: UsersApi,
    }
)
