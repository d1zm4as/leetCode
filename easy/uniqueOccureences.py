class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        uniq = [x for x in set(arr)]#unicos
        lista = [(arr.count(x))for x in uniq]
        
        
        return (len(lista) == len(set(lista)))
        """
        lista = [(arr.count(x))for x in set(arr)]
        return (len(lista) == len(set(lista)))

