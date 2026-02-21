class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2

        while left <= right:
            pivot = left + (right - left) // 2
            guessed_square = pivot * pivot

            if guessed_square == num:
                return True
            elif guessed_square > num:
                right = pivot - 1
            else:
                left = pivot + 1

        return False