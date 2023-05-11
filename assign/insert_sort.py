'''def display(l):
    for i in range(len(l)):
        print(l[i])
'''

def insertion_sort(l):
    for i in range(1,len(l)):
        key = l[i]
        j=i-1
        while j>=0 and key < l[j]:

            l[j+1] = l[j]
            j -= 1
            l[j+1] = key
    print(l)
 

l = [int(x) for x in input().split(',')]
print(l)
insertion_sort(l)
# display(l)
