from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_priority = dict()
        for i in range(len(order)):
            letter_priority[order[i]] = i + 1

        first = 0
        second = 1
        while second < len(words):
            i, j = 0, 0
            while i < len(words[first]) and j < len(words[second]):
                if words[first][i] == words[second][j]:
                    i += 1
                    j += 1
                else:
                    if letter_priority[words[first][i]] < letter_priority[words[second][j]]:
                        break
                    else:
                        return False
            if j >= len(words[second]) and i < len(words[first]):
                return False
            first += 1
            second += 1
        return True