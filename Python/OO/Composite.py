from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(bookTitle):
        self.bookTitle = bookTitle
    def title():
        print("I am the book")
    def content():
        pass
        
class FrontMatter(Book):
    def title():
        print("Front Matter")
    def content():
        print(self.bookTitle)
        print("ISBN: XXXXXXX")

class Chapter(Book):
    def title(chapterTitle):
        print("Chapter: " + chapterTitle)
    def content():
        print("Chapter content here")

class Paragraph(Chapter):
    def title():
        pass
    def content():
        print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

class Figure(Chapter):
    def title(caption):
        self.caption = caption
        print(self.caption)
    def content(imageName):
        print(imageName + " Image displayed here")    

book = Book("Programming Paradigms")
frontMatter = FrontMatter()
chapter1 = Chapter("Java Script")
paragraph1 = Paragraph()
paragraph2 = Paragraph()
figure1 = Figure("Java Script timeline")
chapter2 = Chapter("Python")
paragraph3 = Paragraph()
paragraph4 = Paragraph()
figure1 = Figure("Python Timeline")