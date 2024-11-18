from typing import List

def longestConsecutive(nums:List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if n-1 not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(longest, length)
    return longest

testNums = [0,3,2,5,4,6,1,1]
print(longestConsecutive(testNums))
