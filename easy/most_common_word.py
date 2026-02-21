class Soluton:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        count = Counter(words)
        for word in banned:
            del count[word]
        return count.most_common(1)[0][0]  