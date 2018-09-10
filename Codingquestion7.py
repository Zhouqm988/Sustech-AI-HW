# question 7: ordering three numbers
def exchange(a,b):
    a,b=b,a
    return(a,b)
def revSort(a,b,c) :
    # temps are instrument variables
    temp = max(a,b)
    temp1 = min(a,b)
    temp2 = max(temp,c)
    if(temp == temp2) :
        temp3 = min(temp1,c)
        if (temp1== temp3) :
            return (temp, c ,temp3)
        else :
            return (temp, temp1, c)
    else :
        return (c, temp, temp1)

print(revSort(12,4,32))
# the method below shows the way which take input from user
# a = float(input("input number:"))
# b = float(input("input number:"))
# c = float(input("input number:"))
# print(revSort(a,b,c))








