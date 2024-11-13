from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    hashSet = set()
    for n in nums:
        if n in hashSet:
            return True
        else:
            hashSet.add(n)
    return False

test1 = [1,2,3,1]
test2 = [1,2,3]

print(containsDuplicate(test1))
print(containsDuplicate(test2))



