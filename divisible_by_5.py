a = int(input())
empty_list = []
for i in range(a):
    b = int(input())
    if b % 5 == 0 :
        empty_list += [b]
print(empty_list)