
##### Template for Homework 1, Exercises 1-3 ######


print("********** Homework Exercise 1 **********")

def print_tic_tac_toe():
    v_row = (' '*2 + '|')*2+' '*2
    h_row = '-'*8
    print(v_row)
    print(h_row)
    print(v_row)
    print(h_row)
    print(v_row)

print_tic_tac_toe()


print("********** Homework 1 Exercise 2 **********")

first = input("Enter your first name: ")
last = input("Enter your last name: ")
print("Enter your date of birth:")
month = input("Month? ")
day = input("Day? ")
year = input("Year? ")

print(f"{first} {last} was born on {month} {day}, {year}.")


print("********** Homework 1 Exercise 3 **********")

x = 5
x = x + 6
print(x)

y = 5
y += 6
print(y)
