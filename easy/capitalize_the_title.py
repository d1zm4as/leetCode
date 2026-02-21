#lower words like "of" or other words of lenght 2 or less

class Solution:
    
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        result = []
        for word in words:
            if len(word) > 2:
                result.append(word.capitalize())
            else:
                result.append(word.lower())
        return ' '.join(result)