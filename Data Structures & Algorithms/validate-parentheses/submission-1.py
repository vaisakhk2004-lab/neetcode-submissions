class Solution:
    def isValid(self, s):
        open=['[','{','(']
        close=[']','}',')']
        matching = {')': '(', ']': '[', '}': '{'}
        stack=[]
        for i in range(len(s)):
            if s[i] in open:
               stack.append(s[i])
            elif s[i] in close:
                 if len(stack)==0 or matching[s[i]] != stack.pop():
                    return False
        return len(stack)==0

        