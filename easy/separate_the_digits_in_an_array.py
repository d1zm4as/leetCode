class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        lista = []

        for x in nums:
            for d in str(x):
                lista.append(int(d))

        return lista
        