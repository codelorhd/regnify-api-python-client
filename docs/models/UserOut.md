# regnify.model.user_out.UserOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**is_active** | bool,  | BoolClass,  |  | 
**profile** | [**ProfileOut**](ProfileOut.md) | [**ProfileOut**](ProfileOut.md) |  | 
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**is_super_admin** | bool,  | BoolClass,  |  | 
**[user_roles](#user_roles)** | list, tuple,  | tuple,  |  | 
**email** | str,  | str,  |  | 
**access_begin** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**access_end** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**last_login** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user_roles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MiniUserRoleOut**](MiniUserRoleOut.md) | [**MiniUserRoleOut**](MiniUserRoleOut.md) | [**MiniUserRoleOut**](MiniUserRoleOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

