# set of fruits

fruits = {'apple', 'banana', 'apple', 'chicku'}
print(type(fruits)) # class set
print(fruits)

# an empty set
# es = {} # empty dict

es = set()
print(type(es))


# add a new element to the set
fruits.add('mango')
print(fruits)

fruits.add('apple') # adding duplicate element does not give any error
print(fruits)

fruits.remove('banana')
print(fruits)