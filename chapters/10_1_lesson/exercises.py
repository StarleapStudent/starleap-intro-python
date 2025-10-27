
##### Template for Chapter 10 Exercises 1 - 7, 9 - 12 ######

print("********** Ch 10 Exercise 1 **********")

def nested_sum(integers):
    total = 0
    for item in integers:
        print(f"adding ({type(item)}: {item})")
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += nested_sum(item)
        else:
            print(f"I don't know what to do with type {type(item)}")
    return total

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
t = [[1, 2], [3], [4, 5, 6], 'a']
print(nested_sum(t))



print("********** Ch 10 Exercise 2 **********")

def cumsum(integers):
    sums = []
    total = 0
    for item in integers:
        if isinstance(item, int):
            total += item
            sums.append(total)
    return sums
t = [1, 2, 3]
print(cumsum(t))


print("********** Ch 10 Exercise 3 **********")

def middle(t):
    return t[1:-1]
t = [1, 2, 3, 4, 5]
print(middle(t))



print("********** Ch 10 Exercise 4 **********")

def chop(t):
    del t[0]
    del t[-1]
t = [1, 2, 3, 4]
print(chop(t))
print("t", t)



print("********** Ch 10 Exercise 5 **********")

def is_sorted(t):
    t2 = t[:]
    t2.sort()
    for i in range(len(t)):
        if t[i] != t2[i]:
            return False
    return True
print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))



print("********** Ch 10 Exercise 6 **********")

def is_anagram(word1, word2):
    s1 = list(word1)
    s1.sort()
    print('s1', s1)
    s2 = list(word2)
    s2.sort()
    print('s2', s2)
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True
print(is_anagram('seep', 'pees'))
print(is_anagram('cap', 'paca'))
print(is_anagram('capa', 'pac'))



print("********** Ch 10 Exercise 7 **********")

def has_duplicates(t):
    seen = []
    for item in t:
        if item in seen:
            return True
        seen.append(item)
    return False
print(has_duplicates([1, 2, 3, 1, 4, 5, 6]))
print(has_duplicates([1, 2, 3, 4, 5, 6]))



print("********** Ch 10 Exercise 9 **********")

def get_word_list1():
    words = []
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        words.append(word)
    return words
import time
print('getting word list v1')
t = time.time()
words = get_word_list1()
print(time.time() - t) 

def get_word_list2():
    words = []
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        words = words + [word]
    return words

print('getting word list v2')
t = time.time()
# words = get_word_list2()
print(time.time() - t) 

print("********** Ch 10 Exercise 10 **********")

def in_bisect(sorted_list, word):
    print(f"Searching for {word} between {sorted_list[0]} and {sorted_list[-1]} len {len(sorted_list)}")
    middle_i = len(sorted_list) // 2
    middle_word = sorted_list[middle_i]
    if len(sorted_list) < 10:
        return word in sorted_list
    elif word > middle_word:
        return in_bisect(sorted_list[middle_i:], word)
    else:
        return in_bisect(sorted_list[0:middle_i], word)

print('finding middle by indexing')
t = time.time_ns()
print('middle' in words)
print(time.time_ns() - t)

print('finding middle bisecting')
t = time.time_ns()
print(in_bisect(words, 'middle'))
print(time.time_ns() - t)

def binary_search(word):
    min = 0
    max = len(words) - 1
    while True:
        middle = (min + max) // 2 + 1
        # print(f"min {min}, middle {middle}, max {max}")
        if max == min:
            if words[min] == word:
                return True
            return False
        elif word >= words[middle]:
            min = middle
        else:
            max = middle - 1

def time_binary_search(word):
    print(f"finding {word} binary_search")
    t = time.time_ns()
    print(binary_search(word))
    print(time.time_ns() - t)

time_binary_search('middle')
time_binary_search('weifjawoefj')


print("********** Ch 10 Exercise 11 **********")

def find_reverse_pairs():
    pairs = []

    middle = len(words) // 2 + 1
    for word in words:
        t = list(word)
        t.reverse()
        reverse = ''.join(t)
        if word == reverse:
            continue
        elif word > reverse:
            continue
        if binary_search(reverse):
            pairs.append([word, reverse])
            print(word, reverse)
    print(f"There are {len(pairs)} reverse pairs in the word list.")

print("Reverse pairs:")
find_reverse_pairs()



print("********** Ch 10 Exercise 12 **********")

def gen_interlock(w1, w2):
    w3 = ''
    for i in range(len(w1) -1):
        w3 += w1[i] + w2[i]
    return w3

def uninterlock(w3):
    l3 = list(w3)
    l1 = w3[0::2]
    l2 = w3[1::2]
    w1 = ''.join(l1)
    w2 = ''.join(l2)
    return [w1, w2]

def find_interlocks():
    for word in words:
        [w1, w2] = uninterlock(word)
        if (binary_search(w1) and binary_search(w2)):
            print(f"{w1} + {w2} => {word}")

find_interlocks()

