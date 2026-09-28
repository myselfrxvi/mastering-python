import math
from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        max_pts = 1
        
        for i in range(n):
            # Pruning: If remaining points cannot beat current max or max exceeds n // 2
            if max_pts >= n - i or max_pts > n // 2:
                break
                
            x1, y1 = points[i]
            slopes = defaultdict(int)
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                # Normalize slope fraction using GCD to eliminate float precision errors
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Canonical sign representation
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                    
                slopes[(dy, dx)] += 1
                
            if slopes:
                current_max = max(slopes.values()) + 1  # +1 for points[i] itself
                max_pts = max(max_pts, current_max)
                
        return max_pts
