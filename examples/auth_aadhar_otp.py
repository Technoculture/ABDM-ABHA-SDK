import abha
from abha.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://abhasbx.abdm.gov.in/abha/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = abha.Configuration(
    host="https://abhasbx.abdm.gov.in/abha/api/v3"
)

# Enter a context with an instance of the API client
with abha.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abha.ABHAEnrollmentApi(api_client)
    request_id = 'request_id_example'  # str
    timestamp = 'timestamp_example'  # str
    body = 'body_example'  # str | (optional)

    try:
        # AUTH - OF AADHAAR OTP FOR PARENT VERIFICATION
        api_response = api_instance.api_v3_enrollment_auth_by_aadhaar_post(request_id, timestamp, body=body)
        print("The response of ABHAEnrollmentApi->api_v3_enrollment_auth_by_aadhaar_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ABHAEnrollmentApi->api_v3_enrollment_auth_by_aadhaar_post: %s\n" % e)
