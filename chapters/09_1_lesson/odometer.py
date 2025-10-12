
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1

    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True

def is_palindrome(word):
    word = str(word)
    return is_reverse(word, word)

def find_odometer():
    for number in range(100000, 999999):
        number_str = str(number)
        last_four = number_str[2:]
        if not is_palindrome(last_four):
            continue

        number2 = number + 1
        last_five = str(number2)[1:]
        if not is_palindrome(last_five):
            continue

        number3 = number2 + 1
        middle4 = str(number3)[1:5]
        if not is_palindrome(middle4):
            continue

        number4 = number3 + 1
        if not is_palindrome(number4):
            continue

        print(f"{number} is a match.")
        print(number, 'last four', last_four)
        print(number2, 'last five', last_five)
        print(number3, 'middle 4', middle4)
        print(number4, 'is palindrome')
        print()

find_odometer()
