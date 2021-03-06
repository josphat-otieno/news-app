import os
class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/{}?apiKey={}'
    ARTICLE_API_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    CATEGORY_API_BASE_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    SECRET_KEY= os.environ.get('SECRET_KEY')
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    

class ProdConfig(Config):
    '''
    production configuration child class

    Arg:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}
