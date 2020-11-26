
def calcthegrade():
    score = int(input("Student Score: "))
    percent = round(score / pointspossible, 2)
    print("Precentage is {0}".format(percent))
    grade = "NO GRADE"

    if 1 >= percent >= 0.9:
        grade = "A"
    elif 0.9 > percent >= 0.8:
        grade = "B"
    elif 0.8 > percent >= 0.7:
        grade = "C"
    elif 0.7 > percent >= 0.6:
        grade = "D"
    else:
        grade = "F"


    print("{} - {} - {}".format(studentname, percent, grade ))

pointspossible = 100
studentname = input("Student name: ")
try:
    calcthegrade()
except Exception:
    print("Please provide valid information")
