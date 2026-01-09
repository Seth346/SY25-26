# Grade Calculator
AP = input("Enter Assesment Percent: ")
CP = input("Coursework Percent")
FP = input("Finals Percent: ")
print("Assesment", AP, "Coursework", CP, "Finals", FP)
AG = input("Enter Assesment Grade: ")
CG = input("Enter Coursework Grade: ")
FG = input("Enter Finals Grade: ")
print("Your grade is: ", (float(AP) * float(AG) + float(CP) * float(CG) + float(FP) * float(FG)) / 100)
t1=(AP,CP,FP)
l1=[AG,CG,GP]
l1[1]=10