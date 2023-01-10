# regnify.model.user_create.UserCreate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password** | str,  | str,  |  | 
**last_name** | str,  | str,  |  | 
**first_name** | str,  | str,  |  | 
**email** | str,  | str,  |  | 
**access_begin** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**access_end** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**is_super_admin** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

