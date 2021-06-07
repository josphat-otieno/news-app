import os
class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/{}?apiKey={}'
    ARTICLE_API_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    
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
