class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        result=0
        while i<j:
            area = min(height[i],height[j])*(j-i)
            result=max(area,result)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return result
            

        