from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(title):
        self.bookTitle = bookTitle
        self.title()
    def title(self):
        print(self.bookTitle)
    def content(self):
        pass
        
class FrontMatter(Book):
    def __init__():
        pass
    def title(self):
        print("Front Matter")
    def content(self):
        print(self.bookTitle)
        print("ISBN: XXXXXXX")

class Chapter(Book):
    
    def title(self,chapterTitle):
        print("Chapter: " + chapterTitle)
    def content(self):
        print("Chapter content here")

class Paragraph(Chapter):
    def title(self):
        pass
    def content(self):
        print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

class Figure(Chapter):
    def title(self,caption):
        self.caption = caption
        print(self.caption)
    def content(self,imageName):
        print(imageName + " Image displayed here")    

book = Book("Programming Paradigms")
frontMatter = FrontMatter()
#chapter1 = Chapter("Java Script")
#paragraph1 = Paragraph()
#paragraph2 = Paragraph()
#figure1 = Figure("Java Script timeline")
#chapter2 = Chapter("Python")
#paragraph3 = Paragraph()
#paragraph4 = Paragraph()
#figure1 = Figure("Python Timeline")