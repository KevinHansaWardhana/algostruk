def binSearch(x, target):
    low = 0
    high = len(x) -1
    data = []
    while low != high:
        mid = (high + low) //2
        if x[mid] == target:
            break
        elif target < x[mid]:
            high = mid -1
        else :
            low = mid +1
    for i in range (low, high):
        if target == x[i]:
            data.append(i)
    return data

A=[1,6,2,2,2,6,7,2,9,8,9]
c=2
print(binSearch(A,c))
