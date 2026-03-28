class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        memo = dict(zip(heights,names))
        lista = sorted(heights, reverse = True)
        return [memo[y] for y in lista]

