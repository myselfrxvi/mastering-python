from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        
        parts = s.split('(')
        res = [parts[0]]
        for part in parts[1:]:
            key, rest = part.split(')')
            res.append(d.get(key, '?'))
            res.append(rest)
        return "".join(res)

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard multiple replacements
    assert sol.evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]) == "bobistwoyearsold"
    
    # Test 2: Missing key -> fallback to '?'
    assert sol.evaluate("hi(name)", [["a", "b"]]) == "hi?"
    
    # Test 3: Repeated identical keys
    assert sol.evaluate("(a)(a)(a)aaa", [["a", "yes"]]) == "yesyesyesaaa"
    
    # Test 4: No brackets in string
    assert sol.evaluate("abcde", [["a", "b"]]) == "abcde"
    
    # Test 5: Entire string is a single bracket pair
    assert sol.evaluate("(test)", [["test", "pass"]]) == "pass"
    
    print("ALL TESTS PASSED! Ready for submission.")
