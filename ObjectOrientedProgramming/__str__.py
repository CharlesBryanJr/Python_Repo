'''__str__.py'''
print(" ")

class Page:
    def __init__(self, text, page_number) -> None:
        self.text = text
        self.page_number = page_number
    
    def __len__(self):
        return len(self.text)
    
    def __str__(self):
        return f"Page (text = {self.text}, page_number = {self.page_number})"

class Book:
    def __init__(self, title, author, pages, id_number):
        self.title = title
        self.author = author
        self.pages = pages
        self.id_number = id_number

    def __len__(self):
        return len(self.pages)
    
    def __str__(self):
        output = f"Book (title = {self.title}, author = {self.author}, id_number = {self.id_number})"
        for page in self.pages:
            output += "\n" + str(page)
        
        return output

page1 = Page("Page 1", 1)
page2 = Page("This Page 2", 2)
book = Book("Magum Opus", "Charles", [page1, page2], 33)
print(page1)
print(len(page1))
print(" ")
print(page2)
print(len(page2))
print(" ")
print(book)
print(len(book))


print(" ")

