class Employee:
    
    def __init__(self,e_name,des,sal,otc):
        self.name=e_name
        self.des=des
        self.sal=sal
        self.overTime=otc
        self.status=False

class Organisation:
    
   def __init__(self,emp_list):
      self.employees=emp_list

   def is_eligible(self,th):
       for employee in self.employees:
           otc=employee.overTime
           total_time=0
           for time in otc:
               total_time+=otc[time]
           if (total_time>=th):employee.status=True
   
   def calc_bonus(self,rph):
      total_bonus_pay=0
      for employee in self.employees:
         otc=employee.overTime
         if(employee.status):
            total_time=0
            for time in otc:
               total_time+=otc[time]
            total_bonus_pay+=total_time
      return total_bonus_pay*rph


emps=int(input("How many employees?"))
employees=[]
for _ in range(emps):
   e_name=input("Name of Employee: ")
   des=input("Designation of Employee: ")
   sal=int(input("Salary of Employee: "))
   months_overtime=int(input("No of times worked overtime: "))
   print("Enter details of month and time(in hrs)")
   over_time_cont={}
   for _ in range(months_overtime):
      month=input("Month: ")
      time=int(input("Time(in hrs): "))
      over_time_cont[month]=time
   employee=Employee(e_name,des,sal,over_time_cont)
   employees.append(employee)


threshold=int(input("Enter threshold value: "))
rate=int(input("Pay per hour: "))

org=Organisation(employees)
org.is_eligible(threshold)
bonus_pay=org.calc_bonus(rate)
for employee in employees:
   print(f"{employee.name} {employee.status}")
print(bonus_pay)
