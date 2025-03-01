class Solution:
    def maxArea(self, height: List[int]) -> int:
        li = 0
        ri = len(height)-1
        max_area = 0
        while li<=ri:
            min_height = min(height[li], height[ri])
            area_local = min_height*(ri-li)
            max_area = max(area_local, max_area)
            if height[li]>height[ri]:
                ri-=1
            else:
                li+=1
        return max_area
            
