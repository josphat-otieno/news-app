from flask import render_template,request, redirect, url_for
from . import main
from ..requests import get_articles, get_news_sources,get_top_headlines, get_news_category

@main.route('/')
def index():
    '''
    view root function that returns the idex page and its data
    '''
    title="Welcome to your favorite news app"
    message='Read your favorite news here'
    # getting the sources
    news_sources=get_news_sources('sources')
    top_headlines = get_top_headlines()
    return render_template('index.html', title=title, message=message, sources=news_sources,top_headlines=top_headlines)

@main.route('/article/<id>')
def articles(id):
    '''function to dsiplay articls page and its data
    '''
    articles = get_articles(id)
    title = 'trending articles'
    
    return render_template('article.html' ,articles=articles, title = title)

@main.route('/categories/<category_name>')
def category(category_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_news_category(category_name)
    title = f'{category_name}'
    cat = category_name

    return render_template('categories.html',title = title,category = category, category_name=cat)