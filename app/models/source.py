class Source:
    """
    Source class to define source objects
    """

    def __init__(self, id, title, description, url, category):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.category = category


# id = The News id
# title = The name of the news
# description = A brief description of the news at hand
# url = The Link to the whole news story
# category = Which type of news it falls under