
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def call(f, word):
    print(f"{f}( {word} ) = ", f(word))

call(middle, 'snack')
call(middle, 'bob')
call(middle, 'as')
call(middle, 'a')
call(middle, '')

def is_palindrome(word):
    length = len(word)
    if length <= 1:
        return True
    else:
        f = first(word)
        l = last(word)
        if f != l:
            return False
        else:
            m = middle(word)
            return is_palindrome(m)
        
call(is_palindrome, '')
call(is_palindrome, 'bob')
call(is_palindrome, 'snack')
call(is_palindrome, 'hannah')
call(is_palindrome, 'wasitacaroracatisaw')
call(is_palindrome, "Madam, I'm Adam.")