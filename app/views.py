from flask import render_template
from app import app
from .request import get_sources, get_article

#views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    source = get_sources()
    title = "Home! Welcome to NewsSnooze"
    return render_template('index.html', title=title, sources=source)

@app.route('/article/<id>')
def article(id):
    
    
    articles = get_article(id)
    return render_template('article.html', articles=articles,id=id )