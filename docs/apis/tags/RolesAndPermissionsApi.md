<a name="__pageTop"></a>
# regnify.apis.tags.roles_and_permissions_api.RolesAndPermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_role**](#assign_role) | **post** /roles/{role_id}/assign-role | Assign Role
[**create_role**](#create_role) | **post** /roles/ | Create Role
[**delete_role**](#delete_role) | **delete** /roles/{role_id} | Delete Role
[**edit_role**](#edit_role) | **put** /roles/{role_id} | Edit Role
[**get_role**](#get_role) | **get** /roles/{role_id} | Get Role
[**get_roles**](#get_roles) | **get** /roles/ | Get Roles
[**list_users_assigned_to_role**](#list_users_assigned_to_role) | **get** /roles/{role_id}/list-assigned-users | List Users Assigned To Role
[**unassign_role**](#unassign_role) | **post** /roles/{role_id}/unassign-role | Unassign Role

# **assign_role**
<a name="assign_role"></a>
> UserOut assign_role(role_iduser_id)

Assign Role

Assigns the role to the specified user.                                         <br />                                         <br />                                         <strong>Scopes: </strong> role:create, me,  

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import regnify
from regnify.apis.tags import roles_and_permissions_api
from regnify.model.http_validation_error import HTTPValidationError
from regnify.model.user_out import UserOut
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = regnify.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = regnify.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with regnify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_and_permissions_api.RolesAndPermissionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'role_id': "role_id_example",
    }
    query_params = {
        'user_id': "user_id_example",
    }
    try:
        # Assign Role
        api_response = api_instance.assign_role(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except regnify.ApiException as e:
        print("Exception when calling RolesAndPermissionsApi->assign_role: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id | UserIdSchema | | 


# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
role_id | RoleIdSchema | | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#assign_role.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#assign_role.ApiResponseFor422) | Validation Error

#### assign_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserOut**](../../models/UserOut.md) |  | 


#### assign_role.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_role**
<a name="create_role"></a>
> RoleOut create_role(role_create)

Create Role

Allows an admin to create a role in the system.                                         <br />                                         <br />                                         <strong>Scopes: </strong> role:create, me,  

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import regnify
from regnify.apis.tags import roles_and_permissions_api
from regnify.model.role_out import RoleOut
from regnify.model.http_validation_error import HTTPValidationError
from regnify.model.role_create import RoleCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = regnify.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = regnify.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with regnify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_and_permissions_api.RolesAndPermissionsApi(api_client)

    # example passing only required values which don't have defaults set
    body = RoleCreate(
        title="title_example",
        permissions=[
            "permissions_example"
        ],
    )
    try:
        # Create Role
        api_response = api_instance.create_role(
            body=body,
        )
        pprint(api_response)
    except regnify.ApiException as e:
        print("Exception when calling RolesAndPermissionsApi->create_role: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleCreate**](../../models/RoleCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_role.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_role.ApiResponseFor422) | Validation Error

#### create_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleOut**](../../models/RoleOut.md) |  | 


#### create_role.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_role**
<a name="delete_role"></a>
> AppResponseModel delete_role(role_id)

Delete Role

Deletes the role. This endpoint removes the roles from all users that has been previously assigned. The integer returned is the total number of all users the role has been removed from.                                         <br />                                         <br />                                         <strong>Scopes: </strong> role:delete, me,  

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import regnify
from regnify.apis.tags import roles_and_permissions_api
from regnify.model.app_response_model import AppResponseModel
from regnify.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = regnify.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = regnify.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with regnify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_and_permissions_api.RolesAndPermissionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'role_id': "role_id_example",
    }
    try:
        # Delete Role
        api_response = api_instance.delete_role(
            path_params=path_params,
        )
        pprint(api_response)
    except regnify.ApiException as e:
        print("Exception when calling RolesAndPermissionsApi->delete_role: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
role_id | RoleIdSchema | | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_role.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_role.ApiResponseFor422) | Validation Error

#### delete_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AppResponseModel**](../../models/AppResponseModel.md) |  | 


#### delete_role.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_role**
<a name="edit_role"></a>
> RoleOut edit_role(role_idbody_edit_role_roles_role_id_put)

Edit Role

Updates a single role                                         <br />                                         <br />                                         <strong>Scopes: </strong> role:update, me,  

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import regnify
from regnify.apis.tags import roles_and_permissions_api
from regnify.model.role_out import RoleOut
from regnify.model.http_validation_error import HTTPValidationError
from regnify.model.body_edit_role_roles_role_id_put import BodyEditRoleRolesRoleIdPut
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = regnify.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = regnify.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with regnify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_and_permissions_api.RolesAndPermissionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'role_id': "role_id_example",
    }
    body = BodyEditRoleRolesRoleIdPut(
        title="title_example",
        permissions=[
            "permissions_example"
        ],
    )
    try:
        # Edit Role
        api_response = api_instance.edit_role(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except regnify.ApiException as e:
        print("Exception when calling RolesAndPermissionsApi->edit_role: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyEditRoleRolesRoleIdPut**](../../models/BodyEditRoleRolesRoleIdPut.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
role_id | RoleIdSchema | | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_role.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#edit_role.ApiResponseFor422) | Validation Error

#### edit_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleOut**](../../models/RoleOut.md) |  | 


#### edit_role.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_role**
<a name="get_role"></a>
> RoleOut get_role(role_id)

Get Role

Gets a single role                                         <br />                                         <br />                                         <strong>Scopes: </strong> role:read, me,  

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import regnify
from regnify.apis.tags import roles_and_permissions_api
from regnify.model.role_out import RoleOut
from regnify.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = regnify.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = regnify.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with regnify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_and_permissions_api.RolesAndPermissionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'role_id': "role_id_example",
    }
    try:
        # Get Role
        api_response = api_instance.get_role(
            path_params=path_params,
        )
        pprint(api_response)
    except regnify.ApiException as e:
        print("Exception when calling RolesAndPermissionsApi->get_role: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
role_id | RoleIdSchema | | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_role.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_role.ApiResponseFor422) | Validation Error

#### get_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleOut**](../../models/RoleOut.md) |  | 


#### get_role.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_roles**
<a name="get_roles"></a>
> ManyRolesOut get_roles()

Get Roles

Gets all the roles in the system                                         <br />                                         <br />                                         <strong>Scopes: </strong> role:read, me,  

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import regnify
from regnify.apis.tags import roles_and_permissions_api
from regnify.model.http_validation_error import HTTPValidationError
from regnify.model.many_roles_out import ManyRolesOut
from regnify.model.order_direction import OrderDirection
from regnify.model.order_by import OrderBy
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = regnify.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = regnify.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with regnify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_and_permissions_api.RolesAndPermissionsApi(api_client)

    # example passing only optional values
    query_params = {
        'order_by': None,
        'order_direction': None,
        'title': "title_example",
        'query': "query_example",
        'skip': 0,
        'limit': 100,
    }
    try:
        # Get Roles
        api_response = api_instance.get_roles(
            query_params=query_params,
        )
        pprint(api_response)
    except regnify.ApiException as e:
        print("Exception when calling RolesAndPermissionsApi->get_roles: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
order_by | OrderBySchema | | optional
order_direction | OrderDirectionSchema | | optional
title | TitleSchema | | optional
query | QuerySchema | | optional
skip | SkipSchema | | optional
limit | LimitSchema | | optional


# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | if omitted the server will use the default value of DATE_CREATED

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[OrderBy]({{complexTypePrefix}}OrderBy.md) | [**OrderBy**]({{complexTypePrefix}}OrderBy.md) | [**OrderBy**]({{complexTypePrefix}}OrderBy.md) |  | 

# OrderDirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | if omitted the server will use the default value of DESC

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[OrderDirection]({{complexTypePrefix}}OrderDirection.md) | [**OrderDirection**]({{complexTypePrefix}}OrderDirection.md) | [**OrderDirection**]({{complexTypePrefix}}OrderDirection.md) |  | 

# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SkipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 100

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_roles.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_roles.ApiResponseFor422) | Validation Error

#### get_roles.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ManyRolesOut**](../../models/ManyRolesOut.md) |  | 


#### get_roles.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_users_assigned_to_role**
<a name="list_users_assigned_to_role"></a>
> ManyUserRolesOut list_users_assigned_to_role(role_id)

List Users Assigned To Role

List the users that are assigned to a particular role.                                         <br />                                         <br />                                         <strong>Scopes: </strong> role:read, me,  

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import regnify
from regnify.apis.tags import roles_and_permissions_api
from regnify.model.http_validation_error import HTTPValidationError
from regnify.model.many_user_roles_out import ManyUserRolesOut
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = regnify.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = regnify.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with regnify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_and_permissions_api.RolesAndPermissionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'role_id': "role_id_example",
    }
    try:
        # List Users Assigned To Role
        api_response = api_instance.list_users_assigned_to_role(
            path_params=path_params,
        )
        pprint(api_response)
    except regnify.ApiException as e:
        print("Exception when calling RolesAndPermissionsApi->list_users_assigned_to_role: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
role_id | RoleIdSchema | | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_users_assigned_to_role.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#list_users_assigned_to_role.ApiResponseFor422) | Validation Error

#### list_users_assigned_to_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ManyUserRolesOut**](../../models/ManyUserRolesOut.md) |  | 


#### list_users_assigned_to_role.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **unassign_role**
<a name="unassign_role"></a>
> UserOut unassign_role(role_iduser_id)

Unassign Role

Unassign the role to the specified user.                                         <br />                                         <br />                                         <strong>Scopes: </strong> role:create, me,  

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import regnify
from regnify.apis.tags import roles_and_permissions_api
from regnify.model.http_validation_error import HTTPValidationError
from regnify.model.user_out import UserOut
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = regnify.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = regnify.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with regnify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_and_permissions_api.RolesAndPermissionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'role_id': "role_id_example",
    }
    query_params = {
        'user_id': "user_id_example",
    }
    try:
        # Unassign Role
        api_response = api_instance.unassign_role(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except regnify.ApiException as e:
        print("Exception when calling RolesAndPermissionsApi->unassign_role: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id | UserIdSchema | | 


# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
role_id | RoleIdSchema | | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#unassign_role.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#unassign_role.ApiResponseFor422) | Validation Error

#### unassign_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserOut**](../../models/UserOut.md) |  | 


#### unassign_role.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

