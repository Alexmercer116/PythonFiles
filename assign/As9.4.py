#Assignment 9.4
counts=dict()
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
        word=words[1]
        counts[word]=counts.get(word,0)+1
for key , value  in counts.items():
    if max is None or value > max:
        name=key
        max=value
print(name,max)
