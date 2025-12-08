from collections import defaultdict

def group_words(words):
    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())

print(group_words(["eat", "tea", "tan", "nat"]))



