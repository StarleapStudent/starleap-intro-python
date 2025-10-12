
def has_triple_double(word):
    word = word.casefold()
    double_count = 0
    prev = ''
    for char in word:
        if char == prev:
            double_count = double_count + 1
            # print(f"{word} has a double.")
            if double_count >= 3:
                return True
            prev = ''
        else:
            if prev != '':
                double_count = 0
            prev = char
    return False

# for word in ['allootted', 'abballootted', 'allooted']:
#     result = has_triple_double(word)
#     print(f"{word} has_triple_double ? {result}")

def find_triple_double():
    print("Looking for words with triple double letters...")
    fin = open('shared/words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if has_triple_double(word):
            print(word)
            count = count + 1
    print(f"Found {count} words with a triple double letter.")

find_triple_double()