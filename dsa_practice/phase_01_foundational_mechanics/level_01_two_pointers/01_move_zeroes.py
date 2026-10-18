from typing import List

def move_zeroes(nums: List[int]) -> None:
    """
    Moves all zeroes to the end of nums in-place while maintaining
    the relative order of the non-zero elements.
    
    Time Complexity:  O(N) - single pass with read pointer.
    Space Complexity: O(1) - in-place pointer swapping.
    """
    write = 0
    
    for read in range(len(nums)):
        if nums[read] != 0:
            # Swap non-zero into the write boundary
            nums[write], nums[read] = nums[read], nums[write]
            write += 1

if __name__ == "__main__":
    # Test 1: Standard case with interleaved zeroes
    arr1 = [0, 1, 0, 3, 12]
    move_zeroes(arr1)
    assert arr1 == [1, 3, 12, 0, 0], f"Failed arr1: {arr1}"

    # Test 2: Single element zero
    arr2 = [0]
    move_zeroes(arr2)
    assert arr2 == [0], f"Failed arr2: {arr2}"

    # Test 3: Already clean (no zeroes)
    arr3 = [1, 2, 3, 4]
    move_zeroes(arr3)
    assert arr3 == [1, 2, 3, 4], f"Failed arr3: {arr3}"

    # Test 4: All zeroes
    arr4 = [0, 0, 0]
    move_zeroes(arr4)
    assert arr4 == [0, 0, 0], f"Failed arr4: {arr4}"

    # Test 5: Leading non-zeroes then trailing zeroes
    arr5 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    move_zeroes(arr5)
    assert arr5 == [4, 2, 4, 3, 5, 1, 0, 0, 0, 0], f"Failed arr5: {arr5}"

    print("ALL TESTS PASSED! Fast/Slow Invariant verified.")
