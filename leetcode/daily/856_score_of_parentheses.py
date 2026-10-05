class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack= []
        for i in s:
            if i =="(":
                stack.append(0)
            else:
                v=stack.pop()
                if v==0:
                    stack.append(1)
                else:
                    while stack and stack[-1]!=0:
                        v+=stack.pop()
                    stack.append(v*2+stack.pop())
        return sum(stack)