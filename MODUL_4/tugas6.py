def binSe(x, target):
    low = 0
    high = len(x) -1
    data = []

    while low <= high:
        mid = (high + low) //2
        if x[mid] == target:
            data.append(x.index(target))
            return True
        elif target < x[mid]:
            high = mid -1
        else :
            low = mid +1
    return False
a=[1,2,3,4,5,6,7,8,9,0]
cariA=4
cariB=10
cariC=11
print(binSe(a, cariA))
print(binSe(a, cariB))
print(binSe(a, cariC))
