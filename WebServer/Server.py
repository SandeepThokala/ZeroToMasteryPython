from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')

def dbwriter(data):
	with open('database.txt', mode = 'a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\nid: {email}\nsub: {subject}\nmess: {message}\n\n')

def csvwriter(data):
	with open('database.csv', newline = '', mode = 'a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csvObject = csv.writer(database2, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
		csvObject.writerow([email, subject, message])


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
	if request.method == 'POST': 
		data = request.form.to_dict()
		csvwriter(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong'