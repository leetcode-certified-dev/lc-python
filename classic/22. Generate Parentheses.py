"""
()
()() (())
(())() ()(()) (()()) ((())) ()()()
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        p_set = {"()"}
        for i in range(2, n + 1):
            new_set = set()
            for p in p_set:
                for j in range(len(p)):
                    if p[j] == '(':
                        new_set.add(p[0:j + 1] + "()" + p[j + 1:])
            new_set.add("()" * i)
            p_set = new_set

        return p_set
