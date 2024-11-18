from typing import List

def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    max_area = 0

    while l < r:
        curr_area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, curr_area)

        if (height[l] > height[r]):
            r -= 1
        elif (height[r] > height[l]):
            l += 1
        else:
            l += 1
            r -= 1
    return max_area

testHeight = [1,7,2,5,4,7,3,6]
print(maxArea(testHeight))