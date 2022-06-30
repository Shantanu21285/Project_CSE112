class Student:
    
    def __init__(self,name,cgpa,branch):
        self.n=name
        self.c=cgpa
        self.b=branch
        self.isPlaced=False

    def isEligible(self,company):
        try:
            assert self.c>=company.c
            assert self.isPlaced==False
            assert self.b in company.b
            print(f"STUDENT {self.n} IS ELIGIBLE FOR {company.n}")
            self.apply(company)
        except:
            print(f"STUDENT {self.n} IS NOT ELIGIBLE FOR {company.n}")

    def apply(self,company):
        company.students.append(self)

    def getsPlaced(self):
        self.isPlaced=True

class Company:
    def __init__(self,name,cgpa,branches,positionOpen):
        self.n=name
        self.c=cgpa
        self.b=branches
        self.po=positionOpen
        self.ao=True
        self.students=[]

    def hireStudents(self):
        dict={}
        self.hired=[]
        self.objects_hired=[]
        for i in self.students:
            dict[i.c]=i.n
        order=sorted(dict.items())
        order.reverse()
        k=0
        for i in order:
            if k==self.po:
                break
            self.hired.append(i[1])
            k+=1
        for i in self.students:
            if i.n in self.hired:
                i.getsPlaced()
        Company.closeApplications(self)

    def closeApplications(self):
        self.ao=False
        print(f"THE STUDENTS WHICH COMPANY HIRED ARE: {len(self.hired)}")
        print(*self.hired)

l=[]
# ENTERING DETAILS OF STUDENTS

n=int(input("ENTER THE TOTAL NUMBER OF STUDENTS SITTING FOR PLACEMENTS: "))
for i in range(n):
    name=input(f"ENTER NAME OF STUDENT {i+1}: ")

    while True:
        try:
            cgpa=float(input(f"ENTER THE CGPA OF STUDENT {i+1}: "))
            assert cgpa>0 and cgpa<=10
            break
        except:
            print("INVALID ENTRY. CGPA ENTERED IS LESS THAN ZERO OR GREATER THAN ZERO")

    while True:
        try:
            branch=input(f"ENTER BRANCH OF STUDENT {i+1} (CSE/CSAM/ECE): ")
            assert branch=='CSE' or branch=='CSAM' or branch=='ECE'
            break
        except:
            print("INVALID ENTRY. ONLY CSE, CSAM OR ECE BRANCHES CAN BE FILLED")

    student=Student(name,cgpa,branch)
    l.append(student)

# ENTERING DETAILS BY COMPANY

available=['CSE','CSAM','ECE']
k=int(input("ENTER NUMBER OF COMAPNIES THERE FOR PLACEMENTS: "))
for i in range(k):

    name=input(f"ENTER NAME OF COMPANY {i+1}: ")

    while True:
        try:
            cgpa_r=float(input(f"ENTER REQUIRED CGPA BY COMPANY {i+1}: "))
            assert cgpa_r>0 and cgpa_r<=10
            break
        except:
            print("INVALID CGPA ENTRY")

    while True:
            print("ENTER BRANCHES THE COMPANY WISHES TO PICK STUDENTS FROM WITH SPACES IN BETWEEN")
            branches=[i for i in input().split()]
            flag=True
            for i in branches:
                if i not in available:
                    flag=False
            if flag==True:
                break
            else:
                print('INVALID ENTRY')

    positionsOpen=int(input("ENTER NUMBER OF STUDENTS COMPANY WISHES TO HIRE: "))

    company=Company(name,cgpa_r,branches,positionsOpen)

    for i in l:
        i.isEligible(company)
    company.hireStudents()


            



