# find the target indices if exist or if not find expected indices of a sorted array
num=[1,2,4,6,8]
target = 0
l,r=0,len(num)-1

while l<r :
    mid = (l+r)//2
    if target == num[mid]:
        print(mid)
    elif target > num[mid]:
        l=mid+1
    else :
        r=mid-1
print(l)

    
