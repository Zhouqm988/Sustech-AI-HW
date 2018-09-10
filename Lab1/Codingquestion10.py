# question 10：finding two random integers from 1-10 and exchange their value
import random
def exchange(a,b):
    a,b = b,a
    print("x={1}, y={0}".format(a,b))
x = random.randint(1,10)
y = random.randint(1,10)
print("Output:")
print("x={1}, y={0}".format(x,y))
exchange(x,y)

