def rev (arr, si, ei):
    if si > ei :
        return arr

    arr[si], arr[ei]= arr[ei], arr[si]
    return rev (arr, si + 1, ei-1)


arr = [1,2,3,4,5,6,7,8,9]
print (rev(arr,3,5))