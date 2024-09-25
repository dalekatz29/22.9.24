# START
import statistics

user_list: list[int] = []

for i in range(1, 100 + 1):
    user_list.append(i)

# a
print("# a")
print(user_list)
print()

# b
print("# b")
print(f"1st object: {user_list[0]}")
print()

# c
print("# c")
print(f"last object: {user_list[-1]}")
print()

# d
print("# d")
print(f"len: {len(user_list)}")
print()

# e
print("# e")
e_list: list[int] = []
for i in range(user_list[3 - 1], user_list[12]):
    e_list.append(i)
print(f"From 3 to 12: {e_list}")
print()

# f
print("# f")
f_list: list[int] = []
for i in range(user_list[80 - 1], user_list[-1] + 1):
    f_list.append(i)
print(f"From 80 to end: {f_list}")
print()

# g
print("# g")
g_list: list[int] = []
for i in range(user_list[17]):
    g_list.append(i)
print(g_list)
print()

# h
print("# h")
print(user_list[::-1])
print()

# i
print("# i")
print(user_list[1:len(user_list):2])
print()

# j
print("# j")
for num in user_list:
    if num % 3 == 0:
        print(num, end=" ")
print("\n")

# k
print("# k")
for num in user_list:
    if num % 7 == 0:
        print(num, end=" ")
print("\n")

# l
print("# l")
for num in user_list:
    if num % 10 == 0:
        print(num, end=" ")
print("\n")

# m
print("# m")
print(user_list[-2:66 - 2:-3])
print()

# n
print("# n")
user_list.insert(50, -999)
print(user_list)
user_list.pop(50)
print()

# o
print("# o")
user_list.pop(-1)
print(user_list)

# END
