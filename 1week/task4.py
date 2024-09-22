"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/edit-distance/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ed_dist = [[0] * (len(word1) + 1) for i in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            for j in range(len(word1) + 1):
                if i == 0:
                    ed_dist[i][j] = j
                elif j == 0:
                    ed_dist[i][j] = i
                else:
                    check = ed_dist[i - 1][j - 1] + (
                        1 if word1[j - 1] != word2[i - 1] else 0
                    )

                    ed_dist[i][j] = min(
                        ed_dist[i][j - 1] + 1, ed_dist[i - 1][j] + 1, check
                    )
        return ed_dist[len(word2)][len(word1)]
