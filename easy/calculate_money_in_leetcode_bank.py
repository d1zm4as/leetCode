class Solution:
    def totalMoney(self, n: int) -> int:
        base = n // 7
        soma = base * 28
        soma += (7 * base *( base - 1))//2

        if (n % 7):
            extra = n % 7
            ref = base + 1
            for i in range(extra):
                soma += ref
                ref += 1

        return soma