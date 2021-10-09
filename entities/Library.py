class Library:
    def __init__(self, books_set: {}):
        self.book_set = books_set

    def add_book(self, book):
        self.book_set.append(book)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_json(self):
        return {"title": self.title, "author": self.author}
