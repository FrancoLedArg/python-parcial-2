a = [1, 2]
b = a
a = a + [3]
b.append(4)
print("a:", a)  # [1, 2, 3]
print("b:", b)  # [1, 2, 4]
