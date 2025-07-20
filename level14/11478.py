string = input()

substrings = list()

for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        substrings.append(string[i:j])

substrings = set(substrings)

print(len(substrings))