import abha
from pprint import pprint

# Defining the host is optional and defaults to https://healthidsbx.abdm.gov.in/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(host="https://healthidsbx.abdm.gov.in/api/v1")


# Configure Bearer authorization (JWT): bearerAuth
configuration = abha.Configuration(access_token="")

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.DefaultApi(api_client)
    auth_aadhar_init_request = abha.AuthAadharInitRequest()  # AuthAadharInitRequest |

    try:
        # auth-aadhar-init
        api_response = api_instance.auth_aadhar_init(auth_aadhar_init_request)
        print("The response of DefaultApi->auth_aadhar_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_aadhar_init: %s\n" % e)
