from collections import defaultdict
from typing import List

def groupAnagrams(strs:List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return res.values()

testStrs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

print(groupAnagrams(testStrs))

