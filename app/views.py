from flask import render_template
from app import app

#views
@app.route('/')
def index():

    """
    Views root page function that returns the index page and its data
    """
    message = 'NewsSnooze app'
    return render_template('index.html', message = message)