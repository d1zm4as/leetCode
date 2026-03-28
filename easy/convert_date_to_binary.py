class Solution:
    def convertDateToBinary(self, s: str) -> str:
        # arr = s.split("-")

        # lista = []

        # for x in arr:
        #     lista.append(bin(int(x))[2:])

        # print(lista)

        # ans = "-".join(lista)

        return "-".join([bin(int(x))[2:] for x in s.split("-")])