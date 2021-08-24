import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('8kIqvCK8-5RFVmKhvQZwfM2epvC4hEMyQAaXeWOAP4u2')
assistant = AssistantV2(
    version='2018-11-08',
    authenticator = authenticator
)
url = 'https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/c7182bf5-2097-42f2-adbe-39f0598ad2d9'
assistant.set_service_url(url)
session_id = assistant.create_session(
    assistant_id='35b783ac-e8d4-4f8e-b410-e13828f88b80'
).get_result()["session_id"]



response = assistant.message(
    assistant_id='35b783ac-e8d4-4f8e-b410-e13828f88b80',
    session_id=session_id,
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()

print(json.dumps(response, indent=2))