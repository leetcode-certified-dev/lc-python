dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


class Solution:
    def romanToInt(self, s: str) -> int:
        i, total = 0, 0
        while i < len(s):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i + 1]]:
                total += dic[s[i + 1]] - dic[s[i]]
                i += 2
            else:
                total += dic[s[i]]
                i += 1
        return total

