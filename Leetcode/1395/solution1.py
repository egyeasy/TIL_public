from itertools import combinations

def judge(comb):
    if comb[0] < comb[1] < comb[2]:
        return True
    elif comb[0] > comb[1] > comb[2]:
        return True
    return False

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        
        if len(rating) < 3:
            return count
        
        combs = combinations(rating, 3)
        
        for comb in combs:
            if judge(comb):
                count += 1
        return count