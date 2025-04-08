'''
look at notion Leetcode tracker for more detailed notes on other methods and the different time complexities
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        if len(s) != len(t):
            return False
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        # both have the same keys
        if s_dict == t_dict:
            # check if both have same values
            for key in s_dict.keys():
                if s_dict[key] != t_dict[key]:
                    return False
            return True
        else:
            return False