class LaundryService:

    def __init__(self,name,contact,email,type,branded,season):
        self.name=name
        self.con=contact
        self.email=email
        self.type=type
        if branded==0:
            self.b=False
        else:
            self.b=True
        self.s=season

    def customerDetails(self):
        print(f"Name of customer: {self.name}")
        print(f"Contact of customer: {self.con}")
        print(f"Email of customer: {self.email}")
        print(f"Type of cloth: {self.type}")
        print(f"Branded: {int(self.b)}")
        
    def calculateCharge(self):
        self.charge=0
        if self.type=='Cotton':
            self.charge=50
        elif self.type=='Silk':
            self.charge=30
        elif self.type=='Woolen':
            self.charge=90
        elif self.type=='Polyester':
            self.charge=20

        if self.b==True:
            self.charge*=1.5

        if self.s=='Winter':
            self.charge*=0.5
        else:
            self.charge*=2

        return self.charge

    def finalDetails(self):
        LaundryService.customerDetails(self)
        print(f"Total Charge: {LaundryService.calculateCharge(self)}")
        if self.charge>200:
            print("To be returned in 4 Days!")
        else:
            print("To be returned in 7 Days!")

print("WELCOME TO LAUNDRY SERVICE")
while True:
    try:
        n=int(input("ENTER 1 TO CONTINUE OR ENTER 0 IF YOU WISH TO EXIT: "))
        assert n==0 or n==1
        break
    except:
        print("INVALID ENTRY")

while n==1:
    try:
        print("PLEASE ENTER YOUR DETAILS BELOW CAREFULLY AS WHAT IS ASKED")
        name=input("ENTER YOUR NAME: ")
        contact=int(input("ENTER YOUR CONTACT NUMBER: "))
        assert contact<9999999999
        email=input("ENTER YOUR EMAIL ID: ")
        type=input("ENTER TYPE OF CLOTH: ")
        assert type=='Cotton' or type=='Woolen' or type=='Silk' or type=='Polyester'
        branded=int(input("ENTER BRANDED OR NOT ( 1 IF BRANDED/ 0 IF IT ISN'T BRANDED: "))
        assert branded==0 or branded==1
        season=input("ENTER SEASON: ")
        assert season=='Summer' or season=='Winter'
    except:
        print("INVALID ENTRY")

    id=1

    customer=LaundryService(name,contact,email,type,branded,season)
    customer.finalDetails()
    while True:
        try:
            n=int(input("ENTER 1 TO CONTINUE OR ENTER 0 IF YOU WISH TO EXIT: "))
            assert n==0 or n==1
            break
        except:
            print("INVALID ENTRY")


