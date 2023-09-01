class Employee:
   
   emp_raise= 1.15 #class variable
# To access the class variables you need to access them using 
# class name or class instance or self

   def __init__(self,emp_id,emp_name,emp_role,emp_salary):
      self.emp_id=emp_id
      self.emp_name=emp_name
      self.emp_role=emp_role
      self.emp_salary=emp_salary

   def increase_salary(self,per):
      return self.emp_salary+(per*self.emp_salary)/100
   
class Organization:
   def __init__(self,org_name,emp_list):
      self.org_name=org_name
      self.emp_list=emp_list
   
   def calculate_increment(self,role,per):
      increment_emps = []
      for i in self.emp_list:
         if i.emp_role==role:
            i.emp_salary=i.increase_salary(per)
            increment_emps.append(i)
      return increment_emps

if __name__=="__main__":
   emp1=Employee(1,'Ram','developer',50000)
   emp2=Employee(2,'Shyam','Tester',45000)
   emp3=Employee(3,'Gopal','debugger',40000)
   employees=[emp1,emp2,emp3]
   org=Organization("TCS",employees)
   updated_empsal=org.calculate_increment('developer',12)
   emps=[emp.emp_salary for emp in updated_empsal]
   print(emps)

 
