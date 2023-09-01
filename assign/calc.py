def Add(a,b):return a+b
def Sub(a,b):return a-b
def Multiply(a,b):return a*b
def Divide(a,b):return a/b

operations={
   '+':Add,
   '-':Sub,
   '*':Multiply,
   '/':Divide
}
print(operations['*'](5,2))