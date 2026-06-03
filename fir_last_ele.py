a = int(input())
empty_list = []
for i in range(a):
    b = int(input())
    empty_list += [b]
m = empty_list[:2] + empty_list[-2:]
print(m)