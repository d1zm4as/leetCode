class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half= int(len(s)/2)
        return (len([x for x in s[:half:] if x in "aeiouAEIOU"])==len([x for x in s[half:] if x in "aeiouAEIOU"]))
