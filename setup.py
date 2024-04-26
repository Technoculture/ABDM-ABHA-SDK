# coding: utf-8

"""
    ABHA Enrollment & Profile Management API V3

    It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent. In order to issue an ABHA Number to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily. The ABHA Number will be used for the purposes of uniquely identifying persons and authenticating them. An ABHA Address will be used for threading their health records (only with the informed consent of the patient) across multiple systems and stakeholders.   Notes:   1. In case you want to consume the ABHA APIs and use creation on your own interface, use authentication methods as OTP only.   2. In order to have access to ABHA APIs, your clientId must have hid role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request.   3. In order to have access to Integrated Programs ABHA APIs, your clientId must have integrated_program role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request. Also you will need to share integrated program benefit name to be used in this case.   4. When calling APIs, please ensure that Authorization header must have format as Bearer {Token_Value}. Please note that prefix Bearer is followed by space before the token value.    

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "abha"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="ABHA Enrollment &amp; Profile Management API V3",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "ABHA Enrollment & Profile Management API V3"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent. In order to issue an ABHA Number to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily. The ABHA Number will be used for the purposes of uniquely identifying persons and authenticating them. An ABHA Address will be used for threading their health records (only with the informed consent of the patient) across multiple systems and stakeholders.   Notes:   1. In case you want to consume the ABHA APIs and use creation on your own interface, use authentication methods as OTP only.   2. In order to have access to ABHA APIs, your clientId must have hid role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request.   3. In order to have access to Integrated Programs ABHA APIs, your clientId must have integrated_program role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request. Also you will need to share integrated program benefit name to be used in this case.   4. When calling APIs, please ensure that Authorization header must have format as Bearer {Token_Value}. Please note that prefix Bearer is followed by space before the token value.    
    """,  # noqa: E501
    package_data={"abha": ["py.typed"]},
)
