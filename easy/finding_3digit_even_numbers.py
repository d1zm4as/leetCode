
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        result = set()

        for i in range(100, 1000):
            if i % 2 == 0:
                str_i = str(i)
                if str_i[0] != '0':
                    count_i = Counter(map(int, str_i))
                    if all(count_i[digit] <= count[digit] for digit in count_i):
                        result.add(i)

        return sorted(result)