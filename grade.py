
#När användaren bes om att mata in ett tal så kan programmet krasha om de ej gör Student
# SKapa en try catch som fångar detta och printar ut till konsolen

pointspossible = 100
studentname = input("Student name: ")
def calcgrade():
    percent = score / pointspossible
    grade = "Error"
    ## Bryt ut nedanstående till en metod som heter calcgrade()
    if 1>= percent >= 0.9:
        grade = "A"
    elif 0.9 > percent >= 0.8:
        grade = "B"
    elif 0.8 > percent >= 0.7:
        grade = "C"
    elif 0.7 > percent >= 0.6:
        grade = "D"
    else:
        grade = "fail"
        print("{} - {}".format(studentname, grade))

try:
    score = int(input("Student Score: "))
    calcgrade()
except Exception:
    print("Valid number or something funny maybe:)")
