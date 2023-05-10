fname=input("Enter your Filename: ")
try:
    fh=open(fname)
except:
    print("Invalid Filename")
    quit()
count=0
for line in fh:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        count+=1
        word=line.split()
        print(word[1])
print("There were ", count," lines in the file with From as the first word")
