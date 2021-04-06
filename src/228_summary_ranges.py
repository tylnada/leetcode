# O(N)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        else:
            lst = [nums[0]]
            output = []
            for num in nums[1:]:
                if num == lst[len(lst) - 1] + 1:
                    lst.append(num)
                else:
                    if len(lst) > 1:
                        # print(str(min(lst)) + "->" + str(max(lst)))
                        output.append(str(min(lst)) + "->" + str(max(lst)))
                    else:
                        output.append(str(lst[0]))
                    lst = [num]
            if len(lst) > 1:
                output.append(str(min(lst)) + "->" + str(max(lst)))
            else:
                output.append(str(lst[0]))

            return output

# prettier
class Solution:
    def summaryRanges(self, nums):
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges.append(r)
            r[1:] = [n]
        return ['->'.join(map(str, r)) for r in ranges]
