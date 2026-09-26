from typing import List

class Solution:
    def minMoves(self, source: List[int], target: List[int]) -> int:
        if source == target:
            return 0
        sr, sc = source
        tr, tc = target
        if sr == tr or sc == tc or abs(sr - tr) == abs(sc - tc):
            return 1
        return 2

if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Single diagonal move
    assert sol.minMoves([8, 1], [1, 8]) == 1
    
    # Test 2: Two moves (horizontal then vertical)
    assert sol.minMoves([4, 2], [1, 3]) == 2
    
    # Test 3: Already at target
    assert sol.minMoves([1, 1], [1, 1]) == 0
    
    # Test 4: Same row
    assert sol.minMoves([3, 1], [3, 7]) == 1
    
    # Test 5: Same column
    assert sol.minMoves([2, 5], [8, 5]) == 1
    
    # Test 6: Opposite diagonal
    assert sol.minMoves([2, 2], [5, 5]) == 1
    
    print("ALL TESTS PASSED! Biweekly Contest 192 Q1 verified.")
