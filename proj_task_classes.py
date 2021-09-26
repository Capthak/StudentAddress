class Address():
   
    def set_city(self,city):
        self.city=city
        
    def set_pin(self,pin):
        self.pin=int(pin)
        
    def get_city(self):
        return self.city
    
    def get_pin(self):
        return self.pin

class Student():

    def set_rn(self,rn):
        self.rn=int(rn)

    def set_name(self,name):
        self.name=name

    def set_marks(self,marks):
        self.marks=float(marks)

    def set_add(self,obj):
        self.address=obj

    def get_rn(self):
        return self.rn
    def get_name(self):
        return self.name
    def get_marks(self):
        return self.marks
    def get_add(self):
        return f'{self.address.get_city()},{self.address.get_pin()}'

    
class RollNoInvalid(Exception):
    def __init__(self,msg):
        self.msg=msg
class NameInvalid(Exception):
    def __init__(self,msg):
        self.msg=msg
class MarksInvalid(Exception):
    def __init__(self,msg):
        self.msg=msg
class AddressInvalid(Exception):
    def __init__(self,msg):
        self.msg=msg

def rn():
     a=int(input('enter a roll no'))
     if a<=0:
          raise RollNoInvalid("enter non zero positve no")
     else:
          return a

def nm():
    name=input('enter a name ')
    if name.isalpha()==False:
        raise NameInvalid('enter aplphabets only')
    elif len(name)>20:
        raise NameInvalid('bit too long')
    else:
        return name
def mks():
     mks=int(input("enter marks"))
     
     if mks<0 :
          raise MarksInvalid('enter valid marks')
     elif mks>100:
          raise MarksInvalid('enter valid marks')
     else:
          return mks
def ad_list(l):
    if len(l)<=0:
        raise AddressInvalid("no add to add add some addresses")
    else:
        return True
