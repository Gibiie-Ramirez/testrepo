class Students:
    def __init__(stud, name, math, science, english):
        stud.name = name 
        stud.math = math
        stud.science = science
        stud.english = english

    def ave(stud):
        stud.average = (stud.math + stud.science + stud.english)/3

    def show(stud):
        stud.ave()
        print ("Name: ", stud.name)
        print ("Math Grade: ", stud.math)
        print ("Science Grade: ", stud.science)
        print ("English Grade: ", stud.english)
        if stud.average >= 75:
            stud.status = "Passed"
        else: 
            stud.status = "Failed"
        print("Average Grade: {} ({})".format(round(stud.average,0), stud.status))

print() 
Name = str(input("Enter Name: "))
Math = float(input("Enter Math: "))
Science = float(input("Enter Science: "))
English = float(input("Enter English: "))
print ()
Stud = Students(Name, Math, Science, English)
Stud.show()