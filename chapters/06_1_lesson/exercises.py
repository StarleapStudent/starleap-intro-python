
##### Template for Chapter 5.14, Exercises 1 - 4 ######

print("********** Ch 6 Exercise 1 **********")

print("""
Type your work for Exercise 1 here

    x = 1
    y = 2
    print(c(1, 2+3, 1+2))
      c(1, 5, 3)
        total = 9
        square = b(9)**2
            b(9)
                prod = a(9, 9)
                    a(9, 9)
                        x = 10
                        return 10 * 9 = 90
                prod = 90
                print(9, 90) = "9, 90\n"
                return 90
        square = 90**2 = 8100
        return 8100
    print(8100) = "8100\n"
      
Output:
9, 90
8100   
        
""")


print("********** Ch 6 Exercise 2 **********")

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    
print("ack(3, 4) = ", ack(3, 4))
# print("ack(30, 40) = ", ack(30, 40)) # Results in RecursionError: maximum recursion depth exceeded in comparison


print("********** Ch 6 Exercise 3 **********")

# Exercise 3 should be worked in a new file called palindrome.py



print("********** Ch 6 Exercise 4 **********")

def is_divisible(a, b):
    # print(f"is_divisible( {a}, {b} )")
    if a % b == 0:
        return True
    return False

def is_power(a, b):
    # print(f"is_power( {a}, {b} )")
    if a == b:
        return True
    elif not is_divisible(a, b):
        # print("not divisible")
        return False
    else:
        # print("divisible")    
        return is_power(a/b, b)
    
print("is_power(9, 3) = ", is_power(9, 3))
print("is_power(3, 9) = ", is_power(3, 9))
print("is_power(2048, 4) = ", is_power(2048, 4))


print("********** Ch 6 Exercise 5 **********")

def gcd(a, b):
    # print(f"gcd( {a}, {b} )")
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)
    
print("gcd(9, 9)", gcd(9, 9))
print("gcd(36, 45)", gcd(36, 45))
print("gcd(45, 36)", gcd(45, 36))
print("gcd(100, 35)", gcd(100, 35))
print("gcd(23, 31)", gcd(23, 31))
