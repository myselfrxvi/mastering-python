class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        
        # --- PHASE 1: Precompute Matching Bracket Wormholes ---
        # pair[i] stores the index of the matching '(' or ')' for index i
        pair = {}
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
        curr = 0 
        d = 1
        res = []
        while 0<= curr < n:
            if s[curr] in "()":
                curr = pair[curr]
                d = -d
            else:
                res.append(s[curr])
            curr += d
        return "".join(res)

        