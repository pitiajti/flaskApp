from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

posts = [
	{
		'author': 'Piti Bielicki',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'April 23, 2023',
	},
	{
		'author': 'Ewka Bielicka',
		'title': 'Blog post 2',
		'content': 'Second post content',
		'date_posted': 'April 27, 2023',
	},
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')
    
@app.route("/hello")
def hello():
	return """ <!DOCTYPE html>
 <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>
 <a href="https://www.w3schools.com">This is a link</a> 
</body>
</html> 
"""

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return f'User {escape(username)}'
