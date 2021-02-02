from twilio.rest import Client

account_sid = 'AC0a28f13e5e4ff5bf35a361c1c7b67929'
auth_token = 'fbb26fad273dd01d6ff62904ce05293c'
client = Client(account_sid, auth_token)

message = client.messages.create(from_ = '+12093156264',
								 body = 'Hi, Mr.Sandeep Thokala',
								 to = '+917382990441')

print(message.sid)