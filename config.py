import os

class Config:
    '''
    General confirguration parent class
    '''

    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey=a6cc824aacc54900946fd4ea0c13624e'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?q=bitcoin&apiKey=a6cc824aacc54900946fd4ea0c13624e'
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}