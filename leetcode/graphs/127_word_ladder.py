from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        begin_set = {beginWord}
        end_set = {endWord}
        step = 1
        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            
            next_set = set()
            words -= begin_set
            
            for word in begin_set:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        cand = word[:i] + c + word[i+1:]
                        if cand in end_set:
                            return step + 1
                        if cand in words:
                            next_set.add(cand)
            
            begin_set = next_set
            step += 1
            
        return 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert sol.ladderLength("hit", "hot", ["hot"]) == 2
    print("ALL TESTS PASSED!")