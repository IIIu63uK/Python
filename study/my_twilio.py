from twilio.rest import Client

account_sid = 'AC095b11bd2cf4d5fb2108791715acfc01'
auth_token = 'b64c1b02e1c62637aa26ac3a9d50bce1'
client = Client(account_sid, auth_token)

message = client.messages.create(
from_='+12402407030',
body = 'Test',
to = '+18298507030'
)

print(message.sid)