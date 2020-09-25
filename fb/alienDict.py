# Solution to LC: 953 Verifying Alien Dictionary

'''In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i, c in enumerate(order):
            dic[c] = i
        for i in range(len(words)-1):
            cur = words[i]
            nex = words[i+1]
            for i in range(min(len(cur), len(nex))):
                if cur[i] != nex[i]:
                    if dic[cur[i]] > dic[nex[i]]:
                        return False
                    break
            else:
                if len(cur) > len(nex):
                    return False
        return True
        