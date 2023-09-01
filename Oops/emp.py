class Employeee:
   #  pay_raise = 1.04 -> class variable
    def __init__(self,first,last,pay):
      self.first=first
      self.last=last
      self.pay=pay
      self.email=f'{first}.{last}@fmail.com'
   
    @classmethod
    def ret_str(class_,name):
      first,last,pay=name.split('-')
      return class_(first,last,pay) 
# above @ is a decorator used to create a class method

emp1=Employeee('Mohan','Das',25000)
print(emp1.email)    

emp2='Jonty-Rhodes-30000'
emp=Employeee.ret_str(emp2)
print(emp.email)


