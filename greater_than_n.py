num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
a = int(input())
empty_list = []
for i in num_list :
    if i > a :
        empty_list += [i]
print(empty_list)