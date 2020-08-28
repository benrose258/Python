def myGrade():
    print "Have all your grades ready, and write a guess for the ones you don't have."
    hw1 = input("what's your HW1 grade? ")
    hw2 = input("what's your HW2 grade? ")
    hw3 = input("what's your HW3 grade? ")
    hw4 = input("what's your HW4 grade? ")
    hw5 = input("what's your HW5 grade? ")
    hw6 = input("what's your HW6 grade? ")
    hw7 = input("what's your HW7 grade? ")
    hw8 = input("what's your HW8 grade? ")
    hw9 = input("what's your HW9 grade? ")
    hw10 = input("what's your HW10 grade? ")
    q = input("what is your in class Quiz grade?")
    ex1 = input("what is your Exam 1 grade? ")
    ex2 = input("what is your Exam 2 grade? ")
    ex3 = input("what is your Exam 3 grade? ")
    lab = input('what is your Lab Assignment grade?')
    att = input("what is your attendance score?")
    ex3 = max(ex3, ((ex3/3)+(lab*2/3)))
    hw = (hw1+hw2+hw3+hw4+hw5+hw6+hw7+hw8+hw9+hw10+(q*5))/11*0.2
    if ex1>65 and ex2>65 and ex3>65 and (ex1+ex2+ex3)/3>=80:
        grade = round(hw + att*0.1+(ex1+ex2+ex3)/3*0.7)
        if grade <95:
            print "You are welcome to take the makeup and the final if you want to improve your grade."
        return "your current grade is", grade, "you don't need to take the final."
    else:
        grade = round(hw + att*0.1+(ex1+ex2+ex3)/3*0.45)
        return "your partial grade is: ", grade, "you can still add up to 40 points with 15% of the makeup and 25% of the final."
