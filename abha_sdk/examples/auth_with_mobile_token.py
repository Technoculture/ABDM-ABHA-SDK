import abha
from abha.models.auth_with_mobile_txn_and_user_data import AuthWithMobileTxnAndUserData
from abha.models.jwt_response import JwtResponse
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://healthidsbx.abdm.gov.in/api
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host = "http://healthidsbx.abdm.gov.in/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API key authorization: X-HIP-ID
configuration.api_key['X-HIP-ID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-HIP-ID'] = 'Bearer'

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.AuthenticationApi(api_client)
    auth_request = abha.AuthWithMobileTxnAndUserData() # AuthWithMobileTxnAndUserData | authRequest
    accept_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Authenticate using verified Mobile Number and user data
        api_response = api_instance.auth_with_mobile_token_using_post(auth_request, accept_language=accept_language)
        print("The response of AuthenticationApi->auth_with_mobile_token_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_with_mobile_token_using_post: %s\n" % e)