#question 5:function half_squared
def half_squared(list) :
    newlist=[]
    for item in list :
     x = (item**2)/2
     newlist.append(x)
    print("the output:\n",newlist)

#test the function
half_squared([3,3])

