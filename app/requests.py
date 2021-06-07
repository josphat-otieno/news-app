import urllib.request, json
from .models import Articles, News



# getting the api key
api_key=None

# getting the news base url
base_url= None

# getting the article base url
article_base_url=None

def configue_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url =app.config['NEWS_API_BASE_URL']
    article_base_url=app.config['ARTICLE_BASE_URL']

def get_news_sources(sources):
    '''
    function to get json to our url requests
    '''
    get_news_url =base_url.format(sources,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response=json.loads(get_news_data)
        
        news_results=None

        if get_news_response['sources']:
            movie_results_list=get_news_response['sources']
            news_results = process_results(movie_results_list)

    return news_results

def process_results(news_list):
            '''
            function to process news results and transforms them to a list of objects
        
            args:
                news_list: a list of dictionaries that contains movie details
                Returns:
                movie_list: a list of news objects
            '''
            news_results=[]
            for news_item in news_list:
                id= news_item.get('id')
                name = news_item.get('name')
                url= news_item.get('url')

            
                news_object= News(id,name,url,)
                news_results.append(news_object)

            return news_results       

def get_articles(id):
    '''
    function to get jsonn object to our url request on articles
    '''
    get_article_url=article_base_url.format(id,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        get_articles_data=url.read()
        get_articles_reponse=json.loads(get_articles_data)

        articles_results = None

        if get_articles_reponse['articles']:
            articles_results_list=get_articles_reponse['articles']
            articles_results=process_articles(articles_results_list)

    return articles_results

def process_articles(article_list):
    articles_results=[]

    for article_item in article_list:

        title = article_item.et ('title')         
        author = article_item.get('author')
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')
        

            
        articles_object= Articles(title,author,description,publishedAt,urlToImage,url,)
        articles_results.append(articles_object)

    return articles_results       
