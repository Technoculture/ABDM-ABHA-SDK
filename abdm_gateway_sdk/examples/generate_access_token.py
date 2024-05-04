import abdm_gateway
from abdm_gateway.models.session_request import SessionRequest
from abdm_gateway.models.session_response import SessionResponse
from abdm_gateway.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.abdm.gov.in/gateway
# See configuration.py for a list of all supported configuration parameters.
configuration = abdm_gateway.Configuration(
    host = "https://dev.abdm.gov.in/gateway"
)


# Enter a context with an instance of the API client
with abdm_gateway.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abdm_gateway.SessionsApi(api_client)
    session_request = abdm_gateway.SessionRequest(clientId="",clientSecret="") # SessionRequest | 

    try:
        # Get access token
        api_response = api_instance.v05_sessions_post(session_request)
        print("The response of SessionsApi->v05_sessions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->v05_sessions_post: %s\n" % e)