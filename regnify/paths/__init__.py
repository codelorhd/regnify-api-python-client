# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from regnify.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    TOKEN = "/token"
    ROLES_ = "/roles/"
    ROLES_ROLE_ID = "/roles/{role_id}"
    ROLES_ROLE_ID_ASSIGNROLE = "/roles/{role_id}/assign-role"
    ROLES_ROLE_ID_UNASSIGNROLE = "/roles/{role_id}/unassign-role"
    ROLES_ROLE_ID_LISTASSIGNEDUSERS = "/roles/{role_id}/list-assigned-users"
    USERS_TOKEN = "/users/token"
    USERS_LISTSCOPES = "/users/list-scopes"
    USERS_REQUESTPASSWORDCHANGE = "/users/request-password-change"
    USERS_CHANGEUSERPASSWORD = "/users/change-user-password"
    USERS_ = "/users/"
    USERS_RESENDINVITE = "/users/resend-invite"
    USERS_USER_ID = "/users/{user_id}"
    USERS_USER_ID_ADMINCHANGEUSERPASSWORD = "/users/{user_id}/admin-change-user-password"
