
##### Template for Chapter 7 Exercises 1 - 2 ######

print("********** Ch 7 Exercise 1 **********")

import math

def mysqrt(a):
    epsilon = 0.0000001
    x = a / 2
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x

def pad_str(input, target):
    in_str = str(input)
    l = len(in_str)
    diff = target - l
    return in_str + ' '*diff

def print_table_row(a, b, c, d):
    print(pad_str(a, 4), pad_str(b, 20), pad_str(c, 20), pad_str(d, 20))

def test_square_root():
    print_table_row('a', 'mysqrt(a)', 'math.sqrt(a)', 'diff')
    for a in range(1, 10):
        my_ans = mysqrt(a)
        ans = math.sqrt(a)
        diff = abs(my_ans - ans)
        print(pad_str(a, 4), pad_str(my_ans, 20), pad_str(ans, 20), pad_str(diff, 20))

test_square_root()



print("********** Ch 7 Exercise 2 **********")

def eval_loop():
    result = ''
    while True:
        line = input('> ')
        if line == 'done':
            break
        result = eval(line)
        print(result)
    return result

eval_loop()

