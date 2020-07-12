"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque

adjacent_list = {}
value_map = {}
total_importance = 0


def bfs(id):
    global total_importance
    dq = deque()
    dq.append(id)
    while dq:
        s = dq.popleft()
        total_importance += value_map[s]
        adjacents = adjacent_list[s]
        for c in adjacents:
            dq.append(c)
            

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        global total_importance
        
        total_importance = 0
        
        for em in employees:
            adjacent_list[em.id] = em.subordinates
            value_map[em.id] = em.importance
        
        bfs(id)
        
        return total_importance