class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Return the longest palindromic substring of s."""
    # Manacher's algorithm: O(n) time, O(n) space
    # https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
        if not s:
            return ""
        # Transform s to add separators (e.g., "abc" -> "#a#b#c#") to handle even-length palindromes uniformly
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n  # p[i] = radius of palindrome centered at i
        c = 0  # center of the current rightmost palindrome
        r = 0  # right edge of the current rightmost palindrome
        max_len = 0
        max_center = 0

        for i in range(n):
            mirror = 2 * c - i  # mirror position of i around center c
            if i < r:
                p[i] = min(r - i, p[mirror])  # use previously computed palindrome info

            # Expand around center i
            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            # Update center and right edge if the palindrome expanded past r
            if i + p[i] > r:
                c, r = i, i + p[i]

            # Update max palindrome info
            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        start = (max_center - max_len) // 2  # convert back to original string indices
        return s[start:start + max_len]