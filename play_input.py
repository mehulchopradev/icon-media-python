print('Program starts...')

i = input('Enter n: ')

n = int(i)
print('Odd') if n % 2 else print('Even')

print('Program ends!')

# Python env -> play_input -> int('5') -> 5 -> Odd -> Program ends (Happy flow)
# Python env -> play_input -> int('mehul') -> ValueError -> play_input -> ValueError -> Python env -> prints the error trace