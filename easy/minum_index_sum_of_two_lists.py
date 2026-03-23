class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lista = [] #resposta

        min_idx = float(inf)

        for i in range(len(list1)):
            if list1[i] in list2:
                j =  list2.index(list1[i])
                if i + j < min_idx:
                    min_idx = i + j
                    lista = [list1[i]]
                elif i + j == min_idx:
                    lista.append(list1[i])
                
        return lista
#  forma mais rápida, usa hashmap para buscar os idx mais rapidamente
# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

#         index_map = {word:i for i, word in enumerate(list2)}

#         min_sum = float('inf')
#         result = []

#         for i,word in enumerate(list1):
#             if word in index_map:
#                 sum_index = i + index_map[word]


#                 if sum_index < min_sum:
#                     min_sum = sum_index
#                     result = [word]
#                 elif sum_index == min_sum:
#                     result.append(word)

#         return result    



        
        