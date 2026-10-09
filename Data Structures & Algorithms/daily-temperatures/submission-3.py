class Solution:
    def dailyTemperatures(self, temperatures):
        stack=[]
        output=len(temperatures)*[0]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                        popped=stack.pop()
                        output[popped]=i-popped
            stack.append(i)
        return output
        