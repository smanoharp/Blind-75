def characterReplacement(s: str, k: int) -> int:
    l = 0
    res = 0
    count ={}

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r-l+1)
    return res

# more efficient solution
#  def characterReplacement(s: str, k: int) -> int:
    # l = 0
    # res = 0
    # count ={}
    # maxf = 0

    # for r in range(len(s)):
    #     count[s[r]] = 1 + count.get(s[r], 0)
    #     maxf = max(maxf, count[s[r]])
    #     while (r - l + 1) - maxf > k:
    #         count[s[l]] -= 1
    #         l += 1
    #     res = max(res, r-l+1)
    # return res

testS = "XYYX"
testK = 2

print(characterReplacement(testS, testK))

