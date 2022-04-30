class Config:
    """
    General confguration parent class
    """
    MOVIE_API_BASE_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2022-04-30&sortBy=popularity&apiKey=API_KEY'

class ProdConfig(Config):
    """
    Production cofiguration child class

    Args:
    Config: The parent confguration class with General confguration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class
    
    Args:
    Config: The parent configuration class with general configuration settings
    """

    DEBUG = True

