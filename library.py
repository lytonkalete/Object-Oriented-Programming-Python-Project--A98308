myItems = []

class Choices:
    def myMenu(self):
        print("============Form===============")
        print("1. Login as Admin")
        print("2. Login as Student")

class TodoList(Choices):
    def __init__(self, myItems):
        self.myItems = myItems
        super().__init__()

    def Menu(self):
        print("1. Add Books")
        print("2. View Books")
        print("3. Delete Books")
        print("4. Update Books")
        print("5. Exit")

    def addbooks(self):
        item = input("Enter the Book: ")
        if len(item) >= 1:
            self.myItems.append(item)
            print("Book added successfully!")
        else:
            print("Please enter a Book!")

    def viewbooks(self):
        if not self.myItems:
            print("No Books to show")
        else:
            for index, my_item in enumerate(self.myItems, 1):
                print(f"{index}. {my_item}")
            print(f"There are {len(self.myItems)} books in store")

    def deletebook(self):
        self.viewbooks()
        index = int(input("Enter number for Book to be deleted: "))
        if 1 <= index <= len(self.myItems):
            self.myItems.pop(index - 1)
            print("Book removed successfully!")
        else:
            print("Enter a correct index!")

    def updatebook(self):
        new_item = input("Enter new Book: ")
        index = int(input("Enter index to be replaced: "))
        if 1 <= index <= len(self.myItems):
            self.myItems[index - 1] = new_item
            print("Book updated successfully!")
        else:
            print("Enter a correct index!")

    def exit(self):
        self.myMenu()


class Details(TodoList, Choices):
    def __init__(self):
        
        super().__init__(myItems)

    def Menu(self):
        print("1. Borrow Book")
        print("2. View Book Details")
        print("3. Return Book")
        print("4. Exit")

    def BorrowBook(self):
        borrower = input("Enter your name: ")
        accno = input("Enter access no.: ")
        regno = input("Enter RegNo.: ")
        bookName = input("Enter book to borrow: ")

        if borrower == '' or accno == '' or regno == '' or bookName == '':
            print("Please fill in the correct details below!!")
        else:
            if bookName in self.myItems:
                print("Book borrowed successfully!")
            else:
                print("Book not available for borrowing!")

    def viewbooks(self):
        super().viewbooks()

    def bookDetail(self):
        super().viewbooks()

    def returned(self):
        returned_book = input("Enter the book to be returned: ")
        if returned_book in self.myItems:
            print("Book returned successfully!")
        else:
            print("Book not found in the borrowed list!")

    def exit(self):
        self.myMenu()


class Main:
    def __init__(self):
        while True:
            form = Choices()
            form.myMenu()
            try:
                loginChoice = int(input("Enter Login choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if loginChoice == 1:
                password = "admin"
                adpass = input("Enter admin password: ")
                if adpass == password:
                    while True:
                        p = TodoList(myItems)
                        print("==================Welcome to the library management System======================")
                        p.Menu()
                        try:
                            choice = int(input("Enter choice (1 to 5): "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            continue

                        if choice == 1:
                            p.addbooks()
                        elif choice == 2:
                            p.viewbooks()
                        elif choice == 3:
                            p.deletebook()
                        elif choice == 4:
                            p.updatebook()
                        elif choice == 5:
                            p.exit()
                            break
                        else:
                            print("Invalid choice!")
                else:
                    print("Please provide the correct password!")
            elif loginChoice == 2:
                while True:
                    detail = Details()
                    print("=============welcome student===================")
                    detail.Menu()
                    try:
                        bookchoice = int(input("Enter choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    if bookchoice == 1:
                        detail.BorrowBook()
                    elif bookchoice == 2:
                        detail.bookDetail()
                    elif bookchoice == 3:
                        detail.returned()
                    elif bookchoice == 4:
                        detail.exit()
                        break
                    else:
                        print("Wrong choice")

p2 = Main()





