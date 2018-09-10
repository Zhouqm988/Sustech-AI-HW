# question 12 : print :
# 123456
# 234561
# 345612
# 456123
# 561234
# 612345
list =[]
for i in range(1,7):
    list.append(i)
print("Output:")
for i in range(1,7):
    for item in list[i-1:] :
        print(item,end="")
    for item in list[:i-1]:
        print(item,end="")
    print()
