from typing import List
def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while (l < r):
        m = l + (r-l)//2
        if nums[m] > nums[r]:
            l = m+1
        else:
            r = m
    return nums[l]

testNums = [3,4,5,6,1,2]
print(findMin(testNums))