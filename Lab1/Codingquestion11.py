# question 10: print the diamond
# times are instrument variables, it can be changed into taking numbers from the console
times = 1
times1 = 5
while (times <= 7):
    str = "*"*times
    times = times + 2
    print("{0: ^7}".format(str))
while (times1>=1):
    str = "*"*times1
    times1 = times1 - 2
    print("{0: ^7}".format(str))
