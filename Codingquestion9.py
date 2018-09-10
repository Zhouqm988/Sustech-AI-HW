# question 9: finding special numbers
def find_special_numbers(x):
    cube = x ** 3
    stri = str(cube)
    sum = 0
    while (len(stri) != 0):
        length = len(stri)-1
        a = cube % 10  # get remainder
        sum = sum + a
        b = cube // 10  # exact division calculation
        if (length==0) :
            break
        cube = b
        stri = str(cube)
    if (sum == x ):
        print(x)
print("Output:")
for i in range(1,101) :
    find_special_numbers(i)
