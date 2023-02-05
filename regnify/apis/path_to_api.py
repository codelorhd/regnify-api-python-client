import typing_extensions

from regnify.paths import PathValues
from regnify.apis.paths.token import Token
from regnify.apis.paths.roles_ import Roles
from regnify.apis.paths.roles_role_id import RolesRoleId
from regnify.apis.paths.roles_role_id_assign_role import RolesRoleIdAssignRole
from regnify.apis.paths.roles_role_id_unassign_role import RolesRoleIdUnassignRole
from regnify.apis.paths.roles_role_id_list_assigned_users import RolesRoleIdListAssignedUsers
from regnify.apis.paths.users_token import UsersToken
from regnify.apis.paths.users_list_scopes import UsersListScopes
from regnify.apis.paths.users_request_password_change import UsersRequestPasswordChange
from regnify.apis.paths.users_change_user_password import UsersChangeUserPassword
from regnify.apis.paths.users_ import Users
from regnify.apis.paths.users_resend_invite import UsersResendInvite
from regnify.apis.paths.users_user_id import UsersUserId
from regnify.apis.paths.users_user_id_admin_change_user_password import UsersUserIdAdminChangeUserPassword
from regnify.apis.paths.users_user_id_download_photo import UsersUserIdDownloadPhoto
from regnify.apis.paths.users_user_id_upload_photo import UsersUserIdUploadPhoto

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.TOKEN: Token,
        PathValues.ROLES_: Roles,
        PathValues.ROLES_ROLE_ID: RolesRoleId,
        PathValues.ROLES_ROLE_ID_ASSIGNROLE: RolesRoleIdAssignRole,
        PathValues.ROLES_ROLE_ID_UNASSIGNROLE: RolesRoleIdUnassignRole,
        PathValues.ROLES_ROLE_ID_LISTASSIGNEDUSERS: RolesRoleIdListAssignedUsers,
        PathValues.USERS_TOKEN: UsersToken,
        PathValues.USERS_LISTSCOPES: UsersListScopes,
        PathValues.USERS_REQUESTPASSWORDCHANGE: UsersRequestPasswordChange,
        PathValues.USERS_CHANGEUSERPASSWORD: UsersChangeUserPassword,
        PathValues.USERS_: Users,
        PathValues.USERS_RESENDINVITE: UsersResendInvite,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_ADMINCHANGEUSERPASSWORD: UsersUserIdAdminChangeUserPassword,
        PathValues.USERS_USER_ID_DOWNLOADPHOTO: UsersUserIdDownloadPhoto,
        PathValues.USERS_USER_ID_UPLOADPHOTO: UsersUserIdUploadPhoto,
    }
)

path_to_api = PathToApi(
    {
        PathValues.TOKEN: Token,
        PathValues.ROLES_: Roles,
        PathValues.ROLES_ROLE_ID: RolesRoleId,
        PathValues.ROLES_ROLE_ID_ASSIGNROLE: RolesRoleIdAssignRole,
        PathValues.ROLES_ROLE_ID_UNASSIGNROLE: RolesRoleIdUnassignRole,
        PathValues.ROLES_ROLE_ID_LISTASSIGNEDUSERS: RolesRoleIdListAssignedUsers,
        PathValues.USERS_TOKEN: UsersToken,
        PathValues.USERS_LISTSCOPES: UsersListScopes,
        PathValues.USERS_REQUESTPASSWORDCHANGE: UsersRequestPasswordChange,
        PathValues.USERS_CHANGEUSERPASSWORD: UsersChangeUserPassword,
        PathValues.USERS_: Users,
        PathValues.USERS_RESENDINVITE: UsersResendInvite,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_ADMINCHANGEUSERPASSWORD: UsersUserIdAdminChangeUserPassword,
        PathValues.USERS_USER_ID_DOWNLOADPHOTO: UsersUserIdDownloadPhoto,
        PathValues.USERS_USER_ID_UPLOADPHOTO: UsersUserIdUploadPhoto,
    }
)
