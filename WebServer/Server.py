from flask import Flask, render_template
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
	return render_template('test.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/blog')
def blog():
	return 'ayy, This is my blog..'

@app.route('/blog/2020/dogs')
def blog2():
	return 'This is mah dough.. y\'allz'
