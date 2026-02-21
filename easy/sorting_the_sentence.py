class Solution:

    def sortingSentence(self, s: str) -> str:
        
        sorted_words = sorted(s.split(), key=lambda x: int(x[-1]))
        return ' '.join(word[:-1] for word in sorted_words)