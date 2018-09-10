# question 1: create a list 5 fruits
fruitslist=["apple","pear","orange","pinapple","mandarin"]

#queation 2: go through each fruit and check if it is an apple.
for item in fruitslist :
    if item == "apple" :
        print("question 2 output:")
        print("I found it!")

#question 3: add two new fruits
fruitslist.append("bannana")
fruitslist.append("kiwi")
print("\nquestion 3 output:\n", fruitslist)

#question 4: Create a new empty list. Go through your list of fruits, and for each one,
# add an entry to the new list that tells us how many letters each fruit name is.
# the new list will contain the number of letters of each fruit
numberlist = []
print("\nquestion 4 output:")
for item in fruitslist :
    number = len(item)
    numberlist.append(number)
    print(item + " has " +str(number)+" letters")
    # we use integer number to count the number of letter of each fruit



