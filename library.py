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

from dbutils import connection

def add_new_book():
  title = input('Enter title: ')
  price = float(input('Enter price: '))
  pages = int(input('Enter pages: '))

  con = connection()
  ''' con.execute("insert into books (title, price, pages) values ('{0}', {1}, {2})".format(title, price, pages))
  con.commit() '''
  with con:
    con.execute("insert into books (title, price, pages) values ('{0}', {1}, {2})".format(title, price, pages))
    # it will be commited automatically once it comes out of the with block
  con.close()

def search_books():
  price = float(input('Enter the price: '))
  con = connection()

  sql = 'select * from books where price = {0}'.format(price)
  cursor = con.execute(sql)
  for row in cursor:
    print('{id} | {title} | {pages}'.format(id=row[0], title=row[1], pages=row[-1]))
  else:
    print('No records found!')
  
  con.close()

def delete_book():
  book_id = int(input('Enter the book id: '))
  sql = 'delete from books where id = {0}'.format(book_id)

  con = connection()
  with con:
    con.execute(sql)
  con.close()

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