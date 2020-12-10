def inRange(num, min, max):
    if num > min and num < max:
        return True
    else:
        return False


def dateconvert():
    pass # Question one



# Make user friendly!!

def CSProffessor1():
    print("---CS Proffessor Grade Converter---")
    letter_grades = ['A','B','C','D','F','F'] # List of possible grades
    in_grade = eval(input("Input the students grade: ")) # Check for students grade
    if in_grade <= 5 and in_grade >= 0: # Check if the grade is valid
        print(letter_grades[-in_grade - 1]) # Gets the grade corrosponding to that number
    else:
        print("Invalid Grade")
def CSProffessor2():
    print("--")
    in_grade = eval(input("Input the students grade: "))
    grade = ['A','B','C','D','F'] # List of possible grades
    if inRange(in_grade, 90, 100):
        print(grade[0])
    else:
        if inRange(in_grade, 80, 89):
            print(grade[1])
        else:
            if inRange(in_grade, 70, 79):
                print(grade[2])
            else:
                if inRange(in_grade, 60, 69):
                    print(grade[3])
                else:
                    if in_grade < 60:
                        print(grade[4])





CSProffessor2()