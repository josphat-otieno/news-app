class News:
    '''
    news class to define news objects
    '''

    def __init__(self, id, name, url):
        self.id=id
        self.name=name
        self.url=url
        

class Articles:
    '''
    articles class to define articles objects
    '''
    def __init__(self, title,author, description, publishedAt, urlToImage,url,):
        '''
        method to initialise an object
        '''
        self.title = title
        self.author = author
        self.escription = description
        self.publishedAt = publishedAt
        self.urlToImage = urlToImage
        self.url = url


     
        