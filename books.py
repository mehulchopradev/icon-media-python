import snowflake.connector as snowflake

connection = snowflake.connect(
  user='mehulc',
  password='Snowflake@123',
  account='hw85585.ap-south-1.aws',
  database='LIBRARY_DB'
)

print('Connection established with snowflake!')
print(connection)

# insert a new record in the snowflake database
''' cursor = connection.cursor()
cursor.execute("insert into BOOKS (TITLE, PRICE, PAGES) values ('Book 8', 890, 800)") '''

cursor = connection.cursor()
cursor.execute('select * from BOOKS order by PRICE desc')

''' rows = cursor.fetchall()
for row in rows:
  print('title is {0}'.format(row[0]))
  print('price is {0}'.format(row[1])) '''

batch1 = cursor.fetchmany(4)
print(batch1)

batch2 = cursor.fetchmany(4)
print(batch2)


cursor.close()