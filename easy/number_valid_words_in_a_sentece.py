# A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

# A token is a valid word if all three of the following are true:

#     It only contains lowercase letters, hyphens, and/or punctuation (no digits).
#     There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
#     There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).

# Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

# Given a string sentence, return the number of valid words in sentence.

 

# Example 1:

# Input: sentence = "cat and  dog"
# Output: 3
# Explanation: The valid words in the sentence are "cat", "and", and "dog".

# Example 2:

# Input: sentence = "!this  1-s b8d!"
# Output: 0
# Explanation: There are no valid words in the sentence.
# "!this" is invalid because it starts with a punctuation mark.
# "1-s" and "b8d" are invalid because they contain digits.

# Example 3:

# Input: sentence = "alice and  bob are playing stone-game10"
# Output: 5
# Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
# "stone-game10" is invalid because it contains digits.

 

# Constraints:

#     1 <= sentence.length <= 1000
#     sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
#     There will be at least 1 token.





class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens = sentence.split()
        valid_words = 0

        for token in tokens:
            if self.is_valid_word(token):
                valid_words += 1

        return valid_words

    def is_valid_word(self, token: str) -> bool:
        if any(char.isdigit() for char in token):
            return False

        hyphen_count = token.count('-')
        if hyphen_count > 1:
            return False
        if hyphen_count == 1:
            hyphen_index = token.index('-')
            if hyphen_index == 0 or hyphen_index == len(token) - 1 or not (token[hyphen_index - 1].isalpha() and token[hyphen_index + 1].isalpha()):
                return False

        punctuation_count = sum(token.count(p) for p in ['!', '.', ','])
        if punctuation_count > 1:
            return False
        if punctuation_count == 1:
            punctuation_index = max(token.rfind('!'), token.rfind('.'), token.rfind(','))
            if punctuation_index != len(token) - 1:
                return False

        return True