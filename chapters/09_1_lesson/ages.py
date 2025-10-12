
def is_reverse(num1, num2):
    max_len = max(len(str(num1)), len(str(num2)))
    word1 = str(num1).zfill(max_len)
    word2 = str(num2).zfill(max_len)

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

Max_Age = 110


def count_reverse(offset, max_age = Max_Age):
    count = 0
    for child in range(0, max_age):
        parent = child + offset
        if is_reverse(child, parent):
            count = count + 1
    return count

def find_offset():
    for offset in range(14, 50):
        count = count_reverse(offset)
        if count >= 8:
            return offset

def find_current():
    offset = find_offset()
    for child in range(0, Max_Age):
        parent = child + offset
        if not is_reverse(child, parent):
            continue
        count_so_far = count_reverse(offset, child)
        if count_so_far == 6:
            print(f"He is currently {child} years old, and his mother is {parent} years old.")
            return child

find_current()