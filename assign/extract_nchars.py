str_=input()
n=int(input())
mid=len(str_)//2
print(mid)
if(n>mid):print(str_[mid:])
print(str_[mid:mid+n])
