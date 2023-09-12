def Mergetwosorted(nums1, nums2):
    
    n = len(arr2)
    m = len (arr1) - n
    first_part = nums1[:m] 
    while m > 0 and n> 0 :
        if first_part[m-1] > nums2[n-1]:
            nums1[m+n-1]  = first_part[m -1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    while n > 0:
        nums1[m+n-1] = nums2[n-1]
        n-= 1

    return nums1
arr1 = [1,2,3,0,0,0]
arr2 = [4,5,6]
print (Mergetwosorted(arr1, arr2))