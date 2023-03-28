# PROJECT CODE.

import IPython
b=0
class Library:
    def init(shelf, listOfBooks):
        shelf.books = listOfBooks

    def displayAvailableBooks(shelf):
        print("Books present in this library are: ")
        for book in shelf.books: 
            print(" *" + book)
    
    def borrowBook(shelf, bookName):
        if bookName in shelf.books:
            a=input('Enter your name: ')
            b=input('Enter you gmail ID: ')
            while '@gmail.com'in b:
                break
            while '@gmail.com'not in b:
                print('WRONG ID! Enter the valid ID')
                IPython.display.display(IPython.display.Audio(r"D:\1[94].mp3", autoplay=True))
                print()
                b=input('Enter you gmail ID: ')
                continue
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            shelf.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(shelf, bookName):
        a=input('Enter your name: ')
        b=input('Enter you gmail ID: ')
        while '@gmail.com'in b:
            break
        while '@gmail.com'not in b:
            print('WRONG ID! Enter the valid ID')
            IPython.display.display(IPython.display.Audio(r"D:\1[94].mp3", autoplay=True))
            print()
            b=input('Enter you gmail ID: ')
            continue
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        shelf.books.append(bookName)
        
    
def return_menu():
    print()
    print('''Please choose an option:
              1. Return to main menu
              2. Exit library''')
    global b
    b=int(input("Enter a choice: "))
    if b == 1:
        pass
    while b == 2:
        print("Thanks for choosing Your Library. Have a great day ahead!")
        IPython.display.display(IPython.display.Audio(r"C:\Users\Aryan Walia\OneDrive\Documents\Exit.mp3", autoplay=True))
        break
    if b>2:
        IPython.display.display(IPython.display.Audio(r"D:\1[94].mp3", autoplay=True))
        print('''Invalid Choice!
        choose the correct option''')
        
        
            

class Student: 
    def requestBook(shelf):
        shelf.book = input("Enter the name of the book you want to borrow: ")
        return shelf.book

    def returnBook(shelf):
        shelf.book = input("Enter the name of the book you want to return: ")
        return shelf.book
         

if True:
    YourLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes","CASA","python","basic electronics"])
    student = Student()
    # YourLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ====== WELCOME TO YOUR LIBRARY ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        '''
        IPython.display.display(IPython.display.Audio(r"C:\Users\Aryan Walia\OneDrive\Documents\Welcome.mp3", autoplay=True))
        
        
        while b!=2:
            print(welcomeMsg)
            a = int(input("Enter a choice: "))
            if a == 1:
                YourLibrary.displayAvailableBooks()
                return_menu()

            elif a == 2:
                YourLibrary.borrowBook(student.requestBook())
                return_menu()

            elif a == 3:
                YourLibrary.returnBook(student.returnBook())
                return_menu()

            else:
                IPython.display.display(IPython.display.Audio(r"D:\1[94].mp3", autoplay=True))
                print("Invalid Choice!")
        else:
            break
