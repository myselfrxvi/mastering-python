from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        target_counts = Counter(t)
        need = len(target_counts)
        have = 0
        
        window_counts = {}
        best_len = float("inf")
        best_range = (-1, -1)
        
        left = 0
        for r in range(len(s)):
            c = s[r]
            window_counts[c] = window_counts.get(c, 0) + 1
            if c in target_counts and window_counts[c] == target_counts[c]:
                have += 1
            while have == need:
                if (r - left + 1) < best_len:
                    best_len = r - left + 1
                    best_range = (left, r)
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                left += 1
                
        return "" if best_len == float("inf") else s[best_range[0]:best_range[1] + 1]
