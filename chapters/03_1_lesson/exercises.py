
##### Template for Chapter 3.14, Exercises 1 - 3 ######


print("********** Ch 3 Exercise 1 **********")

def right_justify(input):
    length = len(input)
    print("length = ", length)
    target = 70
    spaces = target - length
    space_string = ' '*spaces
    print(space_string + input)

right_justify('Monty')


print("********** Ch 3 Exercise 2 **********")

# Do your work for Excercise 2 here.

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

def do_four(f):
    do_twice(f)
    do_twice(f)

do_twice(print_spam)
do_four(print_spam)


print("********** Ch 3 Exercise 3 **********")

def draw_h_corner():
    print('+', end=' ')

def draw_h_segment():
    print('-', end=' ')

def draw_h_cell():
    draw_h_corner()
    do_four(draw_h_segment)

def end_h_cell():
    print('+')

def draw_h_lines():
    do_twice(draw_h_cell)
    end_h_cell()

def draw_v_end():
    print('|', end=' ')

def draw_v_segment():
    print(' ', end=' ')

def draw_v_cell():
    draw_v_end()
    do_four(draw_v_segment)

def end_v_cell():
    print('|')

def draw_v_lines():
    do_twice(draw_v_cell)
    end_v_cell()
    
def draw_grid():
    draw_h_lines()
    do_four(draw_v_lines)
    draw_h_lines()
    do_four(draw_v_lines)
    draw_h_lines()
    print(' - '*4+'T')
    one_line = 'hello'
    multi_line = '''
    hi
    I am Emily.
    I love multi-line strings.
    '''

draw_grid()
