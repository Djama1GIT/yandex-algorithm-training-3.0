from collections import Counter

with open("input.txt", 'r') as file:
    c = Counter()
    for i in file:
        string = i.split()
        for word in string:
            for letter in word:
                c[letter] += 1
    letters = sorted(c.keys())
    for i in range(max(c.values()), 0, -1):
        for let in letters:
            print("#" if c[let] >= i else " ", end="")
        print()
    print("".join(letters))

