class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    

    def displayAvailableBooks(self):
        print('\033[1m'+">>> Books present in this library are: ")
        for book in self.books: 
            print("   *" + book)
            
    def borrowBook(self, bookName):
        if bookName in self.books:
            print('\033[1m'+f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            print()
            return True
        else:
            print('\033[1m'+"Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available.")
            print()
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print('\033[1m'+"Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        print()
        
class Student: 
    def requestBook(self):
        self.book = input('\033[1m'+">>> Enter the name of the book you want to borrow: ")
        print()
        return self.book

    def returnBook(self):
        self.book = input('\033[1m'+">>> Enter the name of the book you want to return: ")
        print()
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes","IKIGAI","CASA","Engineering Physics"])
    student = Student()
    
    # centraLibrary.displayAvailableBooks()
    
    while(True):
        welcomeMsg = '\033[1m'+'''\n======📚 Welcome to Central Library 📚======
        
Please choose an option:
1. List all the books
2. Request a book
3. Return a book
4. Exit the Library
        '''+'\033[0m'
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        print()
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print('\033[1m'+"Thanks for choosing Central Library. Have a great day ahead!👋🏻")
            break
        else:
            print('\033[1m'+"⛔Invalid Choice!⛔")
            break
