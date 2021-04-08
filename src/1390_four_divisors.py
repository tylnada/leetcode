class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sumdivs = 0
        for num in nums:
            divs = set()
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    divs.add(i),
                    divs.add(num // i)
                if len(divs) > 4:
                    break
            if len(divs) == 4:
                sumdivs += sum(divs)            
        return sumdivs
