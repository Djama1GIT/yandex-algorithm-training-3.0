from collections import Counter

input_str = input()
counter = Counter()
for i, v in enumerate(input_str):
    counter[v] += int((i + 1) * (len(input_str) - i))
[print(f"{k}: {v}") for k, v in sorted(counter.items())]
