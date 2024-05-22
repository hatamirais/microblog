from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Althemier'}
    posts = [
        {
            'author' : {'username': 'John'},
            'body': 'Post 1'
        },
        {
            'author' : {'username': 'Susan'},
            'body': 'Post 2'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)