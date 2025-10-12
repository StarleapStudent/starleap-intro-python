
##### Template for Chapter 8 Exercises 1 - 5 ######

print("********** Ch 8 Exercise 1 **********")

# Do your work for Excercise 1 here.  

word = 'amazing'
word2 = 'Amazing'
print('casefold', word.casefold() == word2.casefold())

print('123 isnumeric', '123'.isnumeric())

print('Hello! isalnum', 'Hello!'.isalnum())



print("********** Ch 8 Exercise 2 **********")

# Do your work for Excercise 2 here.

fruit = 'banana'
cnt = fruit.count('a')
print('a cnt =', cnt)
print('na cnt =', fruit.count('na'))



print("********** Ch 8 Exercise 3 **********")

# Do your work for Excercise 3 here.

def is_palindrome(word):
    print('is_palindrome()', word)
    return word == word[::-1]
print(is_palindrome('hannah'))
print(is_palindrome('banana'))



print("********** Ch 8 Exercise 4 **********")

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print('''
# Type your answer for Excercise 4 here.

1 - returns false as soon as it finds something not lowercase.  So, it is only accurate if the first letter is lowercase.
      
2 - Same as 1, but returns the strings 'true' or 'false' instead of a boolean.
      
3 - Returns the lowercaseness of the last char in the string.
      
4 - Correctly returns a boolean after traversing the whole string, which is not necessary as soon as any lowercase is found.
      
5 - Returns false if the string contains any non-lowercase chars.

''')



print("********** Ch 8 Exercise 5 **********")

# Do your work for Excercise 5 here.

def rotate_word(word, rot):
    print('rotate_word()', word, rot)
    rot = rot % 26
    new_string = ''
    min = ord('a')
    max = ord('z')
    for letter in word:
        code = ord(letter)
        new_code = code + rot
        while new_code > max:
            new_code = new_code - 26
        while new_code < min:
            new_code = new_code + 26
        new_letter = chr(new_code)
        # print(letter, code, new_code, new_letter)
        new_string = new_string + new_letter
    return new_string

print(rotate_word('helloworld', 15))


def decode_word(encoded):
    print('decode_word()', encoded)
    for i in range(25, 0, -1):
        print('decode_word()', encoded, i)
        word = rotate_word(encoded, i)
        print('rotate_word()', encoded, i, 'returned', word)
        message = 'Rot ' + str(i) + ' : Does the word "' + word + '" make sense? (Y = yes, anything else = no) '
        print('msg', message)
        answer = input(message)
        if answer == 'Y':
            return word
    return 'That was all 26 letters.  Maybe it was a different languange to begin with.'

# encoded = rotate_word('mustard', 67)
# result = decode_word(encoded)
# print(result)
