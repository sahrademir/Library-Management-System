import os


class Book:
    def __init__(self, name, author, release_date, number_of_pages):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"{self.name}, {self.author}, {self.release_date}, {self.number_of_pages}"


class Library:
    def __init__(self, filename='books.txt'):
        self.filename = filename
        if not os.path.isfile(self.filename):
            open(self.filename, 'w').close()

    def add_book(self, book):
        with open(self.filename, 'a') as file:
            file.write(str(book) + '\n')
        print(f'{book.name} Book added successfully\n' + '-' * 20)

    def list_books(self):
        try:
            with open(self.filename, 'r') as file:
                books = file.readlines()
            if books:
                for book in books:
                    name, author, release_date, number_of_pages = book.strip().split(',')
                    print(f'Book Name: {name}\nAuthor Name: {author}\nRelease Date: {release_date}\nNumber of Pages: '
                          f'{number_of_pages}\n' + '-' * 20)
            else:
                print('No books available.')
        except FileNotFoundError:
            print('No books available.')

    def remove_book(self, book_name):
        try:
            with open(self.filename, 'r') as file:
                books = file.readlines()
            with open(self.filename, 'w') as file:
                removed = False
                for book in books:
                    if book_name not in book.split(',')[0]:
                        file.write(book)
                    else:
                        removed = True
                if removed:
                    print(f'{book_name} removed successfully')
                else:
                    print('Book not found.')
        except FileNotFoundError:
            print('No books available.')


lib = Library()

while True:
    choice = input('Menu** \n1.List Books \n2.Add Book \n3.Remove Book\n')

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        name = input('Book Name: ')
        author = input('Author Name: ')
        release_date = input('Release Date: ')
        number_of_pages = input('Number of Pages: ')
        book = Book(name, author, release_date, number_of_pages)
        lib.add_book(book)
    elif choice == "3":
        book_name = input('Enter the name of the book to remove: ')
        lib.remove_book(book_name)
    elif choice == "q":
        break
    else:
        print('Enter a valid option')
