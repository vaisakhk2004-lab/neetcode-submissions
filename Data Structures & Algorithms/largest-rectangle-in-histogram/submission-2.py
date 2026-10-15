class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack=[]
        max_area=0
        for i,val in enumerate(heights):
            start=i
            while stack and stack[-1][1]>val:
                index,value=stack.pop()
                area=(i-index)*value
                max_area=max(max_area,area)
                start=index
            stack.append((start,val))
        for i,val in stack:
            max_area=max(max_area,(len(heights)-i)*val)
        return max_area
        
        