from collections import Counter

k = int(input())
string = input()

left = 0
beauty = 0
maximum = 0
charFreq = Counter()

for right in range(len(string)):
    charFreq[string[right]] += 1
    beauty = max(beauty, charFreq[string[right]])
    while right - left + 1 - beauty > k:
        charFreq[string[left]] -= 1
        left += 1
    maximum = max(maximum, right - left + 1)

print(maximum)