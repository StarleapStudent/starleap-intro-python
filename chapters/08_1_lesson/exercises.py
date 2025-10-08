
##### Template for Chapter 7 Exercises 1 - 5 ######

print("********** Ch 8 Exercise 1 **********")

# Pads an input value with spaces to a specified target length
def pad_str(value, target):
    in_str = str(value)
    l = len(in_str)
    diff = target - l
    return in_str + ' '*diff

# Prints a formatted table row with consistent spacing of columns
def print_table_row(a, b, c, d, length=20):
    print(pad_str(a, length), pad_str(b, length), pad_str(c, length), pad_str(d, length))

# Do your work for Excercise 1 here.  
# Make use of the provided functions above.

print("Ch 8 Exercise 1: Not implemented") # Delete this line when you write your code!


print("********** Ch 8 Exercise 2 **********")

# Do your work for Excercise 2 here.

print("Ch 8 Exercise 2: Not implemented") # Delete this line when you write your code!



print("********** Ch 8 Exercise 3 **********")

# Do your work for Excercise 3 here.

print("Ch 8 Exercise 3: Not implemented") # Delete this line when you write your code!



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


''')

print("Ch 8 Exercise 4: Not implemented") # Delete this line when you write your code!



print("********** Ch 8 Exercise 5 **********")

# Do your work for Excercise 5 here.

print("Ch 8 Exercise 5: Not implemented") # Delete this line when you write your code!

