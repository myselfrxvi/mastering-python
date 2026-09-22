from typing import List

class Node:
    __slots__ = ('remain', 'prod')
    def __init__(self, k: int, val: int = None):
        self.remain = [0] * k
        if val is None:
            self.prod = 1
        else:
            self.remain[val] = 1
            self.prod = val

def merge(left: Node, right: Node, k: int) -> Node:
    node = Node(k)
    node.prod = (left.prod * right.prod) % k
    rem = list(left.remain)
    lp = left.prod
    for i in range(k):
        rem[(i * lp) % k] += right.remain[i]
    node.remain = rem
    return node

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [Node(k) for _ in range(2 * n)]
        
        for i in range(n):
            tree[n + i] = Node(k, nums[i] % k)
            
        for i in range(n - 1, 0, -1):
            tree[i] = merge(tree[i << 1], tree[i << 1 | 1], k)
            
        ans = []
        for idx, val, start, x in queries:
            val %= k
            pos = n + idx
            tree[pos] = Node(k, val)
            pos >>= 1
            while pos > 0:
                tree[pos] = merge(tree[pos << 1], tree[pos << 1 | 1], k)
                pos >>= 1
                
            l = n + start
            r = 2 * n
            res_left = Node(k)
            res_right = Node(k)
            while l < r:
                if l & 1:
                    res_left = merge(res_left, tree[l], k)
                    l += 1
                if r & 1:
                    r -= 1
                    res_right = merge(tree[r], res_right, k)
                l >>= 1
                r >>= 1
            res = merge(res_left, res_right, k)
            ans.append(res.remain[x])
            
        return ans
