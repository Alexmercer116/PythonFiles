class Employee:
   def __init__(self,emp_no,emp_name,leaves):
      self.emp_no=emp_no
      self.emp_name=emp_name
      self.leaves=leaves
   
class Company:
   def __init__(self,cname,emps):
      self.cname=cname
      self.emps=emps
   
   def leave_available(self,emp_no,tolv):
      for emp in self.emps:
         if emp.emp_no==emp_no:
            return emp.leaves[tolv]
   
   def leave_permission(self,emp_no,tolv,nolv):
      for emp in self.emps:
         if emp.emp_no==emp_no and emp.leaves[tolv]>=nolv: return "Granted"
         else: return "Rejected"


if __name__=='__main__':
   c=int(input("How Many: "))
   emps=[]
   z=Company("TCS",emps)
   for i in range(c):
      leaves={}
      emp_no=int(input("Emp_No: "))
      emp_name=input("Emp_Name: ")
      leaves['EL']=int(input("No_Of_EL\'s "))
      leaves['CL']=int(input("No_Of_EL\'s"))
      leaves['SL']=int(input("No_Of_EL\'s"))
      employee=Employee(emp_no,emp_name,leaves)
      z.emps.append(employee)
   emp_id=int(input("Emp_Id: "))
   t_leave=input("Type_Of_Leave: ")
   n_leave=int(input("No_Of_Leaves: "))
   print("Leave_available: ",z.leave_available(emp_no,t_leave))
   print("Permission: ",z.leave_permission(emp_no,t_leave,n_leave))


