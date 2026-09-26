from typing import List

class DifferenceArray:
    """
    Zero-Allocation Difference Array Engine.
    Enables O(1) range updates: update(l, r, val).
    Restores the final array in a single O(N) prefix pass.
    """
    def __init__(self, n: int):
        self.n = n
        # Sizing to n + 1 ensures r + 1 never causes an IndexError when r == n - 1
        self.diff = [0] * (n + 1)

    def update(self, l: int, r: int, val: int) -> None:
        """Add val to all elements in nums[l...r] inclusive in O(1)."""
        self.diff[l] += val
        self.diff[r + 1] -= val

    def build(self) -> List[int]:
        """
        Reconstruct the final array of length self.n in O(N) time
        by accumulating the running prefix sum.
        """
        res = [0] * self.n
        curr = 0
        for i in range(self.n):
            curr += self.diff[i]
            res[i] = curr
        return res

if __name__ == "__main__":
    # Test 1: Single range update
    da1 = DifferenceArray(5)
    da1.update(1, 3, 10)
    assert da1.build() == [0, 10, 10, 10, 0]

    # Test 2: Overlapping updates
    da2 = DifferenceArray(5)
    da2.update(0, 2, 5)   # [5, 5, 5, 0, 0]
    da2.update(2, 4, 3)   # [5, 5, 8, 3, 3]
    assert da2.build() == [5, 5, 8, 3, 3]

    # Test 3: Boundary update reaching the absolute end (r == n - 1)
    da3 = DifferenceArray(4)
    da3.update(0, 3, 7)
    assert da3.build() == [7, 7, 7, 7]

    # Test 4: Negative deltas
    da4 = DifferenceArray(4)
    da4.update(1, 2, -4)
    assert da4.build() == [0, -4, -4, 0]

    print("ALL TESTS PASSED! Difference Array Engine verified.")
