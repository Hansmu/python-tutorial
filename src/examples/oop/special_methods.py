class Book:
    def __init__(self, title, pages):
        self.__title__ = title
        self.__pages__ = pages

    def __str__(self):
        return "The title is " + self.__title__

    def __len__(self):
        return self.__pages__

    def __del__(self):
        print('Book was removed')


def special_methods_example():
    book = Book('Title', 200)

    print(book)
    print(len(book))
    del book
