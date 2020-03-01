from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self,bookTitle):
        self.bookTitle = bookTitle
        self.title()
    def title(self):
        print(self.bookTitle)
    def content(self):
        pass
        
class FrontMatter(Book):
    def __init__(self):
        self.title()
        self.content()
    def title(self):
        print("Front Matter")
    def content(self):
        print("ISBN: XXXXXXX")

class Chapter(Book):   
    def __init__(self,chapterTitle):
        self.chapterTitle = chapterTitle
        self.title()
        self.content()
    def title(self):
        print("Chapter: " + self.chapterTitle)
    def content(self):
        print("Chapter content here")

class Paragraph(Chapter):
    def __init__(self):
        self.title()
        self.content()
    def title(self):
        pass
    def content(self):
        print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

class Figure(Chapter):
    def __init__(self,caption,imageName):
        self.caption = caption
        self.imageName = imageName
        self.title()
        self.content()
    def title(self):
        print(self.caption)
    def content(self):
        print(self.imageName + " Image displayed here")    

book = Book("Programming Paradigms")
frontMatter = FrontMatter()
chapter1 = Chapter("JavaScript")
paragraph1 = Paragraph()
paragraph2 = Paragraph()
figure1 = Figure("JavaScript image","Javascript Timeline")
chapter2 = Chapter("Python")
paragraph3 = Paragraph()
paragraph4 = Paragraph()
figure1 = Figure("Python Image","Python Timeline")