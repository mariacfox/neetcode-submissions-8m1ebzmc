from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        prefs = Counter(students)
        for s in sandwiches:
            if prefs[s] > 0:
                prefs[s] -= 1
            else:
                break
        
        return sum(prefs.values())