
def sort_attribute(op):
    if op=='firstname':
        dict={}
        for i in l:
            dict[i.firstname()]=i.object_list()
        l_det=sorted(dict.items())
        for i,(j,k) in enumerate(l_det):
            print(*k)

    if op=='lastname':
        dict={}
        for i in l:
            dict[i.lastname()]=i.object_list()
        l_det=sorted(dict.items())
        for i,(j,k) in enumerate(l_det):
            print(*k)

    if op=='age':
        dict={}
        for i in l:
            dict[i.age()]=i.object_list()
        l_det=sorted(dict.items())
        for i,(j,k) in enumerate(l_det):
            print(*k)

class Person:
    def __init__(self,first,last,age):
        self.f=first
        self.l=last
        self.a=age

    def object_info(self):
        print(self.f,self.l,self.a)

    def object_list(self):
        return [self.f,self.l,self.a]

    def firstname(self):
        return self.f

    def lastname(self):
        return self.l

    def age(self):
        return self.a

n=int(input("SPECIFY THE NUMBER OF PEOPLE TO BE ENROLLED: "))
l=[]

for i in range(n):
    while True:
        try:
            print("ENTER SPACE SEPERATED DETAILS IN ORDER OF: FIRSTNAME LASTNAME AGE")
            l_element=[i for i in input().split()]
            assert l_element[2].isdigit()
            assert len(l_element)==3
            l_e=[]
            for i in l_element:
                if i.isdigit():
                    l_e.append(int(i))
                else:
                    l_e.append(i)
            per=Person(l_e[0],l_e[1],l_e[2])
            l.append(per)
            break
        except:
            print("INVALID ENTRY")

k=int(input("SPECIFY THE NUMBER OF QUERIES TO BE ENTERED BY THE USER: "))
for i in range(k):
    while True:
        try:
            op=input(f"SPECIFY QUERY {i+1}: ")
            assert op=='firstname' or op=='lastname' or op=='age'
            print("ORDER:")
            sort_attribute(op)
            break
        except:
            print("Invalid Entry")







    
