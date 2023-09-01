def search_string(strings,tar):
   for i,str_ in enumerate(strings):
      if(tar==str_):return i
   return -1

n=int(input())
strings=[]
for i in range(n):
   str_=input()
   strings.append(str_)
print(strings)

target=input()
indx=search_string(strings,target)
if (indx!=-1):
   print(f"Position of searched string is:{indx}")
else:
   print("String not found")
