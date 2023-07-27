from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Index page"
    
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
