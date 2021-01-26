import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'sandeep.thokala98@gmail.com'
email['to'] = 'imdeepu98@gmail.com'
email['subject'] = 'You just won $$ 1 million $$'

email.set_content('I am a Python Master\n\n\nsent with Python programming') 


with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('sandeep.thokala98@gmail.com', 'SANDeep@1998')
	smtp.send_message(email)
	print('all good boss..!!')

 