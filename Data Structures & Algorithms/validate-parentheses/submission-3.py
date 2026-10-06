class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
        }
        for item in s:
            
            if item in pairs.values():
                stack.append(item)
            elif item in pairs.keys():
                if not stack or stack[-1]!=pairs[item]:
                    return False
                stack.pop()
        return len(stack)==0

        
            
            


        