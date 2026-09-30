class Solution:
    def trap(self, heights):
        stack=[]
        output=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]<heights[i]:
                middle=stack.pop()
                if not stack:
                    break
                left=stack[-1]
                height=min(heights[left],heights[i])-heights[middle]
                width=i-left-1
                output+=width*height
            stack.append(i)
        return  output

        
        