from typing import List

def twoSum(nums:List[int], target) -> List[int]:
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

testNums = [2, 7, 11, 15]
testTarget = 9
print(twoSum(testNums, testTarget))
