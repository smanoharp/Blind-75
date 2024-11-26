from typing import List

def search(nums: List[int], target: int) -> int:

    #find pivot
    l, r = 0, len(nums) - 1
    while (l < r):
        m = l + (r-l)//2
        if(nums[m] > nums[r]):
            l = m+1
        else:
            r = m
    start = l
    l = 0
    r = len(nums) - 1

    #find position of target
    if(target >= nums[start] and target <= nums[r]):
        l = start
    else:
        r = start
    
    #basic bs
    while(l <= r):
        m = l + (r-l)//2
        if (nums[m] == target):
            return m
        elif(target > nums[m]):
            l = m+1
        else:
            r = m-1
    return -1

testNums = [3,4,5,6,1,2]
testTarget = 1
print(search(testNums, testTarget))
