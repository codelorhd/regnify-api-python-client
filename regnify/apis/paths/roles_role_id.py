from regnify.paths.roles_role_id.get import ApiForget
from regnify.paths.roles_role_id.put import ApiForput
from regnify.paths.roles_role_id.delete import ApiFordelete


class RolesRoleId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
