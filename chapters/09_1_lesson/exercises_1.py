
##### Template for Chapter 9.2 Exercises 1 - 6 ######

print("********** Ch 9.2 Exercise 1 **********")

def more_than_20():
    print("Words with more than 20 characters:")
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
    print()

more_than_20()



print("********** Ch 9.2 Exercise 2 **********")

def has_no_e(word=''):
    try:
        index = word.casefold().index('e')
        return False
    except ValueError:
        return True
print('self', has_no_e('self'))
print('happy', has_no_e('happy'))

def print_has_no_e():
    print("Words with no 'e'")
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            print(word)
    print()

print_has_no_e()



print("********** Ch 9.2 Exercise 3 **********")

def avoids(word, forbidden):
    for char in forbidden:
        try:
            word.index(char)
            return False
        except ValueError:
            continue
    return True
print('self', 'be', avoids('self', 'be'))
print('happiness', 'bcdfg', avoids('happiness', 'bcdfg'))

def prompt_avoids():
    print("This program will display a list of words that don't contain any forbidden characters.")
    forbidden = input('What characters are forbidden? ').strip()
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            print(word)
    print()
# prompt_avoids()

def count_blocked(forbidden):
    count = 0
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            continue
        else:
            count = count + 1
    # print(f"{count} words were blocked by {forbidden}")
    return count
# count_blocked('j')
# count_blocked('k')
# count_blocked('v')
# count_blocked('x')
# count_blocked('z')

def find_uncommon_chars():
    low_group = ''
    for code in range(ord('a'), ord('z')):
        char = chr(code)
        blocked = count_blocked(char)
        if blocked <= 8900:
            print(f"{blocked} words contain {char}")
            low_group = low_group + char
    return low_group
low_group = find_uncommon_chars()
print(f"{low_group} blocked {count_blocked(low_group)} words")




print("********** Ch 9.2 Exercise 4 **********")

def uses_only(word, letters):
    word = word.casefold()
    letters = letters.casefold()
    print(f"Checking {word} for chars:{letters}")
    for char in word:
        try:
            index = letters.index(char)
        except ValueError:
            return False
    return True
print('Hoe alfalfa', 'acefhlo', uses_only('Hoe alfalfa', 'acefhlo '))




print("********** Ch 9.2 Exercise 5 **********")

def uses_all(word, required):
    word = word.casefold()
    required = required.casefold()
    # print(f"Does {word} use all of the letters {letters}?")
    for letter in required:
        if letter not in word:
            return False
    return True
uses_all('face', 'ace')
uses_all('false', 'ace')

def find_uses_all(letters):
    count = 0
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        if uses_all(word, letters):
            count = count + 1
            print(word)
    print(f"{count} words use all the letters {letters}.")
find_uses_all('aeiou')
find_uses_all('aeiouy')




print("********** Ch 9.2 Exercise 6 **********")

def is_abecedarian(word):
    word = word.casefold()
    prev_char = 'a'
    for char in word:
        if char < prev_char:
            return False
        prev_char = char
    return True

def find_abecedarian():
    count = 0
    longest = ''
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            count = count + 1
            print(word)
            if len(word) > len(longest):
                longest = word
    print(f"There are {count} abecedarian words.")
    print(f"The longest abecedarian word is {longest} with a length of {len(longest)}.")
find_abecedarian()


