class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        nums = [num for num in range(1, m + 1)]
        result = []
        
        for query in queries:
            for i in range(m):
                if query == nums[i]:
                    result.append(i)
                    nums.insert(0, nums.pop(i))
                    break
        
        return result
