#q1
a=input("a: ")
b=input("b: ")
c=input("c: ")
sum=int(a)+int(b)+int(c)
average=sum/3
print("average",average)

#q2
Gross_income=input("gross income: ")
no_of_dependents=input("no of independents: ")
standard_deductions=10000
dependent_deduction=1000
Taxable_income=int(Gross_income)-int(standard_deductions)-int(dependent_deduction)*int(no_of_dependents)
Tax_rate=0.20
Tax=int(Taxable_income)*Tax_rate
print(f'${Tax}')

#q(3)
#q3
Name=input("Name: ")
SID=input("SID: ")
Gender=input("Gender: ")
Course_name=input("Course_name")
CGPA=input("CGPA: ")
List=[Name,int(SID),Gender,Course_name,float(CGPA)]
print(List)


#q(4)
Subject1_Marks=input("Marks: ")
Subject2_Marks=input("Marks: ")
Subject3_Marks=input("Marks: ")
Subject4_Marks=input("Marks: ")
Subject5_Marks=input("Marks: ")
List=(Subject1_Marks,Subject2_Marks,Subject3_Marks,Subject4_Marks,Subject5_Marks)
my_list=sorted(List)
print(my_list)

#q5(a)
colours=["Red","Green","White","Black","Pink","Yellow"]
colours.remove("Black")
print(colours)
 
#q5b
colours=["Red","Green","White","Black","Pink","Yellow"]
colours[3:5]=["Purple"]
print(colours)
 


 

