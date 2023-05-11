fname = input("Enter file name: ")
count=0
total=0
result=0
try:
    fh = open(fname)
except:
    print("Invalid Filename")
    quit()
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count+=1
        total+=float(line[20:-1])
try:
    result=total/count
except:
    if count==0 or total==0:
        print("No Required Words Found")
        quit()
print("Average spam confidence:",result)
