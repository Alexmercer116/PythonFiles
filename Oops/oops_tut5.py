class Product:
   def __init__(self,pid,pname,barcode):
      self.pid=pid
      self.pname=pname
      self.barcode=barcode
class Company:
   def __init__(self,prod_list):
      self.prod_list=prod_list
   def checkDigit(self,id):
      