#question 6: change scores into grade
# the"&" doesn't support different type but "and" can
def scores_change_grade(a) :

    if(a>=90 and a<=100) :
        grade = "A"
        print("the grade is:", grade)
    elif(a>60 and a<=89) :
        grade = "B"
        print("the grade is:", grade)
    elif(a>=0 and a<=60) :
        grade = "C"
        print("the grade is:", grade)
    else :
        print("Invalid scores enter")

a = float(input("input scores:"))
scores_change_grade(a)
