def is_triangle(a, b, c):
    print('is_triangle()', a, b, c)
    if a >= b + c:
        print('No')
    elif b >= a + c:
        print('No')
    elif c >= a + b:
        print('No')
    else:
        print("Yes")

is_triangle(3, 4, 5)
is_triangle(2, 1, 1)
is_triangle(0, 0, 0)

# Ask user for input - 3 sides of sticks
# then print out whether it's a triangle
a = float(input('How long is side a? '))
print('a is', a, type(a))
b = float(input('How long is side b? '))
print('b is', b, type(b))
c = float(input('How long is side c? '))
print('c is', c, type(c))

is_triangle(a, b, c)