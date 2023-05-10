counts=dict()
lst=list()
max=None
name=None
try:
    fh=open(input("Enter Your File Name : "))
except:
    print("Invalid Filename!!")
    print("\nEnter Proper Filename")
    quit()
for line in fh:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        words=line.split()
        word=words[5].split(':')
        counts[word[0]]=counts.get(word[0],0)+1
#print(sorted([(k,v)  for k,v in counts.items()]))
for k,v in counts.items():
    lst.append((k,v))
lst.sort()
for key,value in lst:
    print(key,value)
