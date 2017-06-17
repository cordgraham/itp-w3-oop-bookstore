class Bookstore(object):
    def __init__(self, name):
      self.name = name
      self.books = []  
    
    def get_books(self):
      return self.books
    
    def add_book(self, Book):
      self.books.append(Book)
    
    def search_books(self, title="/( O o )/ ", author=None):
      listofbooksbyauthor = []
      listofbooksbytitle = []
      for book in self.books:
        if title.lower() in book.title.lower():
          listofbooksbytitle.append(book)
        elif book.author == author:
          listofbooksbyauthor.append(book)
      if len(listofbooksbyauthor) != 0:
        return listofbooksbyauthor
      else:
        return listofbooksbytitle
    
class Author(object):
    def __init__(self, name, nationality):
      self.name = name
      self.nationality = nationality
      self.books = []
  
    def get_books(self):
      return self.books
      
class Book(object):
    
    def __init__(self, title, author):
      self.title = title
      self.author = author
      author.books.append(self)