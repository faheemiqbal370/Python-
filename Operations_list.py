lst = [10, 20, 30, 20]

print("Original  List:", lst)

lst.append(40)
print("append(40):", lst)

lst.extend([50, 60])
print("extend([50, 60]):", lst)


lst.insert(1, 15)
print("insert(1, 15):", lst)

lst.remove(20)
print("remove(20):", lst)



p = lst.pop()
print("pop():", lst, "| Popped:", p)

print("index(30):", lst.index(30))

print("count(20):", lst.count(20))

lst.reverse()
print("reverse():", lst)


lst.sort()
print("sort():", lst)

new_list = lst.copy()
print("copy():", new_list)

print("len():", len(lst))

print("min():", min(lst))

print("max():", max(lst))

print("sum():", sum(lst))

print("Is 30 in list?", 30 in lst)

del lst[0]
print("del lst[0]:", lst)

