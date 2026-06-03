a = int(input())
b = int(input())
empty_list = []
for i in range(a):
    c = int(input())
    empty_list += [c]
for i in range(b):
    d = int(input())
    print(empty_list[d])