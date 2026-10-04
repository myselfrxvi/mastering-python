class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Greedy approach tracking the range of possible open '(' counts.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        cmin = 0  # Minimum possible open '(' count
        cmax = 0  # Maximum possible open '(' count

        for ch in s:
            if ch == '(':
                cmin += 1
                cmax += 1
            elif ch == ')':
                cmin -= 1
                cmax -= 1
            else:  # ch == '*'
                cmin -= 1  # '*' treated as ')'
                cmax += 1  # '*' treated as '('

            # If cmax < 0, even converting every '*' to '(' isn't enough to balance ')'
            if cmax < 0:
                return False

            # cmin cannot drop below 0 (can treat '*' as empty string or '(' instead of ')')
            cmin = max(cmin, 0)

        # Valid if 0 is within the possible range of open parentheses count
        return cmin == 0


    def checkValidStringTwoStacks(self, s: str) -> bool:
        """
        Alternative approach using two stacks storing indices.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        open_stack = []
        star_stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                open_stack.append(i)
            elif ch == '*':
                star_stack.append(i)
            else:  # ch == ')'
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        # Match remaining '(' with '*' that appear after them
        while open_stack and star_stack:
            if open_stack[-1] > star_stack[-1]:
                return False
            open_stack.pop()
            star_stack.pop()

        return len(open_stack) == 0


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
        (")(", False),
        ("(((***", True),
        ("***(((", False),
        ("(((*)))", True),
    ]

    for s, expected in test_cases:
        res = sol.checkValidString(s)
        assert res == expected, f"Failed for {s}: got {res}, expected {expected}"
        print(f"'{s}' -> {res} (Passed)")
