fname = input("Enter file name: ")
with open(fname,'r') as fh:
    lst=list()
    for line in fh:
        l=line.split()
        for i in l:
            if i not in lst:
                lst.append(i)
print(lst)

