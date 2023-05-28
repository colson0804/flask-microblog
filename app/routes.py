from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Craig'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        }, 
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was just okay!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)