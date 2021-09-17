'''
Welcome to my library system
1. Add a new book
2. Search for a book
3. Delete a book
4. Exit
Please enter ur choice: 1
Enter title: Book 1
Enter price: 900
Enter pages: 560
Book Added!
1. Add a new book
2. Search for a book
3. Delete a book
4. Exit
Please enter ur choice: 2
Enter the price: 900
1 | Book 1 | 560
2 | Book 2 | 700
1. Add a new book
2. Search for a book
3. Delete a book
4. Exit
Please enter ur choice: 3
Enter the book id: 2
Book Deleted!
1. Add a new book
2. Search for a book
3. Delete a book
4. Exit
Please enter ur choice: 4
'''

import sqlite3

def add_new_book():
  title = input('Enter title: ')
  price = float(input('Enter price: '))
  pages = int(input('Enter pages: '))

  con = sqlite3.connect('/Users/mehulchopra/Documents/training/kh/icon-media-dataanalytics/library_db.db')
  con.execute("insert into books (title, price, pages) values ('{0}', {1}, {2})".format(title, price, pages))
  con.commit()
  con.close()

def search_books():
  pass

def delete_book():
  pass

while True:
  print('Welcome to my library system')
  print('1. Add a new book', '2. Search for a book', '3. Delete a book', '4. Exit', sep='\n')
  choice = int(input('Please enter ur choice: '))

  if choice == 1:
    add_new_book()
  elif choice == 2:
    search_books()
  elif choice == 3:
    delete_book()
  else:
    break