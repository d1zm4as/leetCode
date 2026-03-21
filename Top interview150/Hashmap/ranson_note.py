from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hr = Counter(ransomNote)

        hm = Counter(magazine)

        for x in ransomNote:
            if hr[x]>hm[x]:
                return False
        return True



# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         for i in ransomNote:
#             if i in magazine:
#                 magazine=magazine.replace(i,'',1)
#             else:
#                 return False
#         return True
            



        