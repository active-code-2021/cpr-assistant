from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('8kIqvCK8-5RFVmKhvQZwfM2epvC4hEMyQAaXeWOAP4u2')
assistant = AssistantV2(
    version='{version}',
    authenticator=authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/c7182bf5-2097-42f2-adbe-39f0598ad2d9/v1/workspaces/0bd30a50-c7b1-464e-9eee-2eca1cdc79cc/message')

assistant.set_disable_ssl_verification(True)