 def singleNumber(self, arr: List[int]) -> int:
        result = 0
        
        for num in arr:
            result = result ^ num
            
        return result