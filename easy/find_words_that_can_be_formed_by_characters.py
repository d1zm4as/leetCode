from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        soma = 0

        for x in words:
            if not Counter(x) - Counter(chars):
                soma += len(x)

        return soma