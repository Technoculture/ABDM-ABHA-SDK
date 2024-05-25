# coding: utf-8

"""
    Abdm Abha

    Abdm SDK for abha

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from abha.models.profile_share2_request_one_of import ProfileShare2RequestOneOf

from abha.api_client import ApiClient, RequestSerialized
from abha.api_response import ApiResponse
from abha.rest import RESTResponseType


class AbdmAppProfileShareApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def profile_share_4(
        self,
        profile_share2_request_one_of: ProfileShare2RequestOneOf,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=1)] = 0,
    ) -> None:
        """This API will be invoked by the HIP for sharing the response of HIECM's /api/v3/hiecm/profile/share API

        This is a API will be invoked by the <b>HIP</b> to share the response of HIECM's /api/v3/hiecm/profile/share API. <ol type='1'> <li> <b>Header</b>  <ol type='a'> <br/> <li>Authorization will be provided by the gateway session API after the successful verification of client ID and Secret [ Example: eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJ2YXNhbnRoYWt1bWFyLmtlc2F2 ]</li> <li>REQUEST_ID unique UUID[ Example: 18235d89-cb13-479d-ad71-7a57d5f669a8 ]</li> <li>TIMESTAMP  actual time of the requested was initiated[ Example: 2022-10-06T10:10:00.587 ]</li> <li>X_HIU_ID  HIU ID[ Example: ABDM_SBX ]</li> </ol> </li> <br/> <li> <b>Request Body</b> <ol type='a'><br/> <li>acknowledgement is mandatory object in case of successful response</li> <li>error is optional object in case of successful response</li> <li>response is mandatory object in both the cases</li> </ol> </ol>

        :param profile_share2_request_one_of: (required)
        :type profile_share2_request_one_of: ProfileShare2RequestOneOf
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._profile_share_4_serialize(
            profile_share2_request_one_of=profile_share2_request_one_of,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '408': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def profile_share_4_with_http_info(
        self,
        profile_share2_request_one_of: ProfileShare2RequestOneOf,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=1)] = 0,
    ) -> ApiResponse[None]:
        """This API will be invoked by the HIP for sharing the response of HIECM's /api/v3/hiecm/profile/share API

        This is a API will be invoked by the <b>HIP</b> to share the response of HIECM's /api/v3/hiecm/profile/share API. <ol type='1'> <li> <b>Header</b>  <ol type='a'> <br/> <li>Authorization will be provided by the gateway session API after the successful verification of client ID and Secret [ Example: eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJ2YXNhbnRoYWt1bWFyLmtlc2F2 ]</li> <li>REQUEST_ID unique UUID[ Example: 18235d89-cb13-479d-ad71-7a57d5f669a8 ]</li> <li>TIMESTAMP  actual time of the requested was initiated[ Example: 2022-10-06T10:10:00.587 ]</li> <li>X_HIU_ID  HIU ID[ Example: ABDM_SBX ]</li> </ol> </li> <br/> <li> <b>Request Body</b> <ol type='a'><br/> <li>acknowledgement is mandatory object in case of successful response</li> <li>error is optional object in case of successful response</li> <li>response is mandatory object in both the cases</li> </ol> </ol>

        :param profile_share2_request_one_of: (required)
        :type profile_share2_request_one_of: ProfileShare2RequestOneOf
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._profile_share_4_serialize(
            profile_share2_request_one_of=profile_share2_request_one_of,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '408': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def profile_share_4_without_preload_content(
        self,
        profile_share2_request_one_of: ProfileShare2RequestOneOf,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=1)] = 0,
    ) -> RESTResponseType:
        """This API will be invoked by the HIP for sharing the response of HIECM's /api/v3/hiecm/profile/share API

        This is a API will be invoked by the <b>HIP</b> to share the response of HIECM's /api/v3/hiecm/profile/share API. <ol type='1'> <li> <b>Header</b>  <ol type='a'> <br/> <li>Authorization will be provided by the gateway session API after the successful verification of client ID and Secret [ Example: eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJ2YXNhbnRoYWt1bWFyLmtlc2F2 ]</li> <li>REQUEST_ID unique UUID[ Example: 18235d89-cb13-479d-ad71-7a57d5f669a8 ]</li> <li>TIMESTAMP  actual time of the requested was initiated[ Example: 2022-10-06T10:10:00.587 ]</li> <li>X_HIU_ID  HIU ID[ Example: ABDM_SBX ]</li> </ol> </li> <br/> <li> <b>Request Body</b> <ol type='a'><br/> <li>acknowledgement is mandatory object in case of successful response</li> <li>error is optional object in case of successful response</li> <li>response is mandatory object in both the cases</li> </ol> </ol>

        :param profile_share2_request_one_of: (required)
        :type profile_share2_request_one_of: ProfileShare2RequestOneOf
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._profile_share_4_serialize(
            profile_share2_request_one_of=profile_share2_request_one_of,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '408': None,
            '500': None,
            '503': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _profile_share_4_serialize(
        self,
        profile_share2_request_one_of,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _hosts = [
            'https://integrator.callback.url'
        ]
        _host = _hosts[_host_index]

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if profile_share2_request_one_of is not None:
            _body_params = profile_share2_request_one_of



        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/[callback_url]/v3/app/patient/profile/on-share',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


