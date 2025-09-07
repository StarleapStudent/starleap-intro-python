
##### Template for Chapter 5.14, Exercises 1 - 4 ######


print("********** Ch 5 Exercise 1 **********")

def time_since_epoch():
    import time
    t = time.time()
    sec_per_minute = 60
    sec_per_hour = sec_per_minute * 60
    sec_per_day = sec_per_hour * 24

    days = int(t / sec_per_day)
    remainder = t % sec_per_day
    hours = int(remainder / sec_per_hour)
    remainder = remainder % sec_per_hour
    minutes = int(remainder / sec_per_minute)
    remainder = remainder % sec_per_minute
    seconds = int(remainder)

    print(f"It has been {days} days, {hours} hours, {minutes} minutes, {seconds} seconds since the epoch.")

time_since_epoch()


print("********** Ch 5 Exercise 2 **********")

def check_fermat(a, b, c, n):
    left_side = a**n + b**n
    right_side = c**n
    if (n > 2 and left_side == right_side):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def fermat_prompt():
    print("Let's check Fermat's Last Theorem.")
    a = int(input("Give me a value for a "))
    b = int(input("Give me a value for b "))
    c = int(input("Give me a value for c "))
    n = int(input("Give me a value for n "))
    check_fermat(a, b, c, n)

fermat_prompt()


print("********** Ch 5 Exercise 3 **********")

def is_triangle(a, b, c):
    if (a >= b + c or b >= a + c or c >= a + b):
        print("No")
    else:
        print("Yes")

def triangle_prompt():
    print("Let's see if these sticks can make a traingle.")
    a = int(input("What is the length of stick 1? "))
    b = int(input("What is the length of stick 2? "))
    c = int(input("What is the length of stick 3? "))
    print("Can the sticks form a triangle?")
    is_triangle(a, b, c)

triangle_prompt()


print("********** Ch 5 Exercise 4 **********")

answer = """
recurse(n=3, s=0) {
    recurse(n=2, s=3) {
        recurse(n=1, s=5) {
            recurse(n=0, s=6) {
                print(6)
            }
        }
    }
}
"""
print(answer)
