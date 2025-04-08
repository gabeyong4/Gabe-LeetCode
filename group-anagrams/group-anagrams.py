from collections import defaultdict
class Solution:
    # O(NlogN) time complexity and O(N) space complexity
    def groupAnagramsOne(strs):
        dic = dict()
        sorted_strs = list()
        final_lst = []
        for word in strs:
            temp_lst = sorted(word)
            sorted_strs.append(tuple(sorted(word)))

        for index in range(len(strs)):
            if sorted_strs[index] not in dic:
                dic[sorted_strs[index]] = []
                dic[sorted_strs[index]].append(strs[index])
            else:
                dic[sorted_strs[index]].append(strs[index])
                
        for val in dic.values():
            final_lst.append(val)
        return final_lst

    def groupAnagramsSolution(strs):
        nested_dict = defaultdict(list)
        for word in strs:
            # create an array with 26 positions to correspond to the 26 characters in the alphabet
            count = [0] * 26
            for char in word:
                position = ord(char) - ord("a")
                count[position] += 1
            nested_dict[tuple(count)].append(word)
        return nested_dict.values()

strs = ["act","pots","tops","cat","stop","hat"]
print(Solution.groupAnagramsOne(strs))
print(Solution.groupAnagramsSolution(strs))