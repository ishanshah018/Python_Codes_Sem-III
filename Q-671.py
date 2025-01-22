class Book:
    def __init__(self, name, n, authors, publisher, isbn, year):
        self.name = name
        self.n = n
        self.authors = authors
        self.publisher = publisher
        self.isbn = isbn
        self.year = year

    def display(self):
        print(f"Book: {self.name}\nAuthors: {', '.join(self.authors)}\nPublisher: {self.publisher}\nISBN: {self.isbn}\nYear: {self.year}")

class CourseBook(Book):
    def __init__(self, name, n, authors, publisher, isbn, year, course):
        super().__init__(name, n, authors, publisher, isbn, year)
        self.course = course

    def display(self):
        super().display()
        print(f"Course: {self.course}")

book = CourseBook("Python Programming", 2, ["Author A", "Author B"], "Tech Publisher", "12345", 2021, "CS101")
book.display()
