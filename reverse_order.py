a = int(input())
empty_list= []
for i in range(a):
    b = input()
    empty_list = [b] + empty_list
    
for i in empty_list:
    print(i)