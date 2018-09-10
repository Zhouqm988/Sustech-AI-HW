# question 8: change two-dimensional array into a sequence
# may be can extend to n
def two_dim_arrs_traverse(list):
    list1 = list[0]
    list2 = list[1]
    list3 = []
    for item in list1 :
        list3.append(item)
    for item in list2 :
        list3.append(item)
    print("Output:")
    for item in list3 :
        print(item,end=" ")


# test
list1 = [1,2,3]
list2 = [4,5,6]
list = [list1,list2]
two_dim_arrs_traverse(list)
# the method below shows an other way take input from the console
# list1 = list(input("\nthe one dimensional array1(without any character):"))
# list2 = list(input("the one dimensional array2:"))
# list = [list1,list2]
# two_dim_arrs_traverse(list)


