#naive
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n+1):
            if i % 15 == 0:
                output += 'FizzBuzz',
            elif i % 5 == 0:
                output += 'Buzz',
            elif i % 3 == 0:
                output += 'Fizz',
            else:
                output += str(i),
        return output

#genius
class Solution:
    def fizzBuzz(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
