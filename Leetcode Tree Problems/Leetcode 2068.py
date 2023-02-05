class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1 = {}
        for i in range(len(word1)):
            if word1[i] not in count1:
                count1[word1[i]] = 1
            else:
                count1[word1[i]] += 1
        for i in range(len(word2)):
            if word2[i] not in count1:
                count1[word2[i]] = -1
            else:
                count1[word2[i]] -= 1
        for i in count1.keys():
            if abs(count1[i]) > 3:
                return False
        return True