import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Sandeep Thokala'
email['to'] = 'imdeepu98@gmail.com'
email['subject'] = 'you just won $$ 10 million $$ in cash'
email.set_content(html.substitute(name = 'Sandyiee..'), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('sandeep.thokala98@gmail.com', 'SANDeep@1998')
	smtp.send_message(email)
	print('all good cap..!!')
