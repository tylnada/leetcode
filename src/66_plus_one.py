class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        q = 0
        for i in reversed(range(len(digits))):
            q, r = divmod(digits[i] + 1, 10)
            digits[i] = r
            if q == 0:
                break
            else:
                if i == 0:
                    digits.insert(0, q)
        return digits
