from typing import List
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        layer = {beginWord}
        parents = defaultdict(list)
        found = False
        
        while layer and not found:
            words -= layer
            next_layer = set()
            for word in layer:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        cand = word[:i] + c + word[i+1:]
                        if cand in words:
                            if cand == endWord:
                                found = True
                            next_layer.add(cand)
                            parents[cand].append(word)
            layer = next_layer
            if not layer:
                return []
            
        res = []
        def dfs(curr, path):
            if curr == beginWord:
                res.append(path[::-1])
                return
            for p in parents[curr]:
                dfs(p, path + [p])
        dfs(endWord, [endWord])
        return res
        