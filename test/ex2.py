from book import Book

library = [
    Book("asd", "dsa"),
    Book("qwe", "ewq"),
    Book("zxc", "cxz")
]

for book in library:
    print(f"{book.name} - {book.author}")
    