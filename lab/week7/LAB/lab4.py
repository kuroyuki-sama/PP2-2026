# Book 클래스 (p. 527)
class Book:
    def __init__(self, title, page):
        self.title, self.page = title, page

    def __le__(self, other): return self.page < other.page
    def __lt__(self, other): return self.page <= other.page
    def __ge__(self, other): return self.page > other.page
    def __gt__(self, other): return self.page >= other.page

b1 = Book("title1", 800)
b2 = Book("title2", 900)
print(b1 < b2)