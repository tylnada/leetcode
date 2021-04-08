# greatest common divisor function used
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)
        divisor = gcd(len(str1), len(str2))
        return str1[:divisor] if str1[:divisor] * (len(str2)//divisor) == str2 and str2[:divisor] * (len(str1)//divisor) == str1 else ''
