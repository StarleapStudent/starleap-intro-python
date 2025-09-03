
def print_lyrics():
    print('Boots')
    print('Cats')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    print_lyrics()

# repeat_lyrics()

def print_twice(input):
    print(input)
    print(input)

# print_twice('Spam'*4)

def is_it_even(input):
    if input % 2 == 0:
        print(str(input) + ' is even')
    else:
        print(str(input) + ' is odd')

# is_it_even(4)
# is_it_even(5)

x = 5
y = 6

def compare(x, y):
    if x < y:
        print(str(x) + ' is less than ' + str(y))
    elif x > y:
        print(str(x) + ' is greater than ' + str(y))
    else:
        print(str(x) + ' must equal ' + str(y))

compare(7, 6)

print('out here, x is', x, ' and y is', y)





