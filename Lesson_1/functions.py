# minimal element

def minimal(l):
    min1 = l[0]
    for i in l:
        if i < min1:
            min1 = i
    print (min1)

nums1 = [1, 2, -3, 0, 7]
minimal(nums1)