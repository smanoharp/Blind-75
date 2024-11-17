from typing import List

def topKFrequent(nums:List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    # initialize freq list with empty list elements

    for n in nums:
        count[n] = 1 + count.get(n,0)
    # updating count dict with number and its count in the nums

    for n, c in count.items():
        freq[c].append(n)
    # updating freq with index as count and respective numbers to the count

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if (len(res) == k):
                return res

testNums = [1,2,2,3,3,3]
testK = 2

print(topKFrequent(testNums, testK))