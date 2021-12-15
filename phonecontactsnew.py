Contacts=[{"Firstname":"Dinesh","Lastname":"Kumar","mobile":8838924827,"Emailid":"dineshgmail.com"},
          {"Firstname":"Bala","Lastname":"Swetha","mobile":8838924822,"Emailid":"swethagmail.com"},
          {"Firstname":"viji","Lastname":"amma","mobile":9095351365,"Emailid":"vijigmail.com"},
          {"Firstname":"Muthu","Lastname":"Karuppan","mobile":9698163075,"Emailid":"muthugmail.com"},
          {"Firstname":"Raja","Lastname":"Prabhu","mobile":9791252940,"Emailid":"rajagmail.com"},
          {"Firstname":"Anu","Lastname":"Priya","mobile":8838925552,"Emailid":"anugmail.com"},
          {"Firstname":"Arun","Lastname":"Vijay","mobile":9023451365,"Emailid":"arungmail.com"},
          {"Firstname":"Sree","Lastname":"Ram","mobile":9876163075,"Emailid":"sreegmail.com"},
          {"Firstname":"Bharath","Lastname":"Kumar","mobile":9123451365,"Emailid":"bharathgmail.com"},
          {"Firstname":"vijay","Lastname":"Sharma","mobile":9876163075,"Emailid":"vijaygmail.com"}]

print(Contacts)
class Mobile_Contacts:
    def __init__(self,number):
        self.number=number

    def viewcontacts(self):
        if self.number==1:
            Firstname=input("Enter Firstname")
            lastname=input("Enter Lastname")
            Mobile=input("Enter Number")
            Emailid=input("Email id")
            print(obj.savecontacts(Firstname,lastname,Mobile,Emailid))
    
        elif self.number==2:
            Firstname=input("Enter Firstname")
            print(obj.deletecontacts(Firstname))

        elif self.number==3:
            Firstname=input("Enter name")

            print(obj.searchcontacts(Firstname))
        print(Contacts)
        
            

    def savecontacts(self,Firstname,Lastname,Mobile,Emailid):
        self.Firstname=Firstname
        self.Lastname=Lastname
        self.Mobile=Mobile
        self.Emailid=Emailid
        phonecontacts=str(self.Mobile)
        
        
        if type(self.Firstname)==str and type(self.Lastname)==str and type(phonecontacts)==str and type(self.Emailid)==str:
            if (len(self.Firstname)<=10) and (len(self.Lastname) <=10) and (len(phone_contact) == 10) and (len(self.Emailid)<=25):
                Contacts.append({"Firstname":self.Firstname,"Lastname":self.Lastname,"Mobile":int(phonecontacts),"Emailid":self.Emailid})
                return "contact saved"
            else:
                raise ValueError("error occured")
        else:
            raise TypeError("error occured")

    def deletecontacts(self,Firstname):
        for i in Contacts:
            if i['Firstname']==Firstname :
                i.clear()
                print("contact deleted")
                
    def searchcontacts(self,Firstname):
        search=[]
        for i in Contacts:
            if i['Firstname']==Firstname:
                search.append(i)
                print(search)
        


    
#object1=Mobile_Contacts()
#object1.viewcontacts()


print(" 1.Save 2.Delete 3.search contact ")
Firstname=int(input("enter number"))
#Firstname=int(input("enter numbernumber"))
#obj=Contacts(Firstnumber)
obj=Mobile_Contacts(Firstname)
obj.viewcontacts()










    
