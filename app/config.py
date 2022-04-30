class Config:
    """
    General confguration parent class
    """
    pass

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

    Debug = True

