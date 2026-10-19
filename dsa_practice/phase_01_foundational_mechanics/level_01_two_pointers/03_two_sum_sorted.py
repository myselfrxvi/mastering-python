from typing import List

def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    Find two numbers in a sorted array that add up to target.
    Returns 1-based indices [index1, index2].
    
    Time:  O(N) - opposite boundary squeeze.
    Space: O(1) - two integer pointers.
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        curr = numbers[left] + numbers[right]
        if curr == target:
            return [left + 1, right + 1]  # 1-based indexing
        elif curr > target:
            right -= 1
        else:
            left += 1
            
    return []

if __name__ == "__main__":
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_sorted([-1, 0], -1) == [1, 2]
    print("ALL TESTS PASSED! Two Sum Sorted Inward Squeeze verified.")
