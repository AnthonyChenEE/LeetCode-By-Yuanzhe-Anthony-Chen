# Yuanzhe Chen UNSW EE
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        res1 = ""
        res2 = ""
        while len(word1) > 0 and len(word2) > 0:
            res1 = word1[0]
            word1 = word1[1:]

            res2 = word2[0]
            word2 = word2[1:]

            res += res1 + res2

        res += word1 + word2
        return res