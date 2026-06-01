a = int(input())
empty_list = []
for i in range(a):
    b = input()
    empty_list += [b]
    
    
print(empty_list[0:3]+empty_list[-3:])