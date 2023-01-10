# regnify.model.role_out.RoleOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date_created** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**[permissions](#permissions)** | list, tuple,  | tuple,  |  | 
**can_be_deleted** | bool,  | BoolClass,  |  | 
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**title** | str,  | str,  |  | 
**created_by_user** | [**UserOut**](UserOut.md) | [**UserOut**](UserOut.md) |  | 
**modified_by_user** | [**UserOut**](UserOut.md) | [**UserOut**](UserOut.md) |  | [optional] 
**date_modified** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# permissions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

