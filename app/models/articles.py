class Article:
    """
    A class that generates new instances of news articles within news sources
    """
    
    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


# author = The sole author of the article
# title = this is the main heading of the article
# description = a brief overview of the articles
# url = a link to the article
# urlToImage = image link
# publishedAt = the Date of publish
