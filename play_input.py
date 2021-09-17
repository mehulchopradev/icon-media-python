from traceback import print_exc

''' print('Program starts...')

i = input('Enter n: ')

n = int(i)
print('Odd') if n % 2 else print('Even')

print('Program ends!') '''

# Python env -> play_input -> int('5') -> 5 -> Odd -> Program ends (Happy flow)
# Python env -> play_input -> int('mehul') -> ValueError -> play_input -> ValueError -> Python env -> prints the error trace


# Python env -> play_input -> int('mehul') -> ValueError -> play_input (handle the error)
# try -- except block

print('Program starts...')

while True:
  i = input('Enter n: ')

  ''' try:
    n = int(i)
    print('Odd') if n % 2 else print('Even')
    break
  except ValueError:
    print('Hey please enter numeric values only!')
    # print the detailed trace of the error
    print_exc() '''

  try:
    n = int(i)
  except ValueError:
    print('Hey please enter numeric values only!')
    # print the detailed trace of the error
    print_exc()
  except Exception:
    print_exc()
  else:
    # these stmts will execute when there is no error in the corresponding try block
    print('Odd') if n % 2 else print('Even')
    break

print('Program ends!')