"""
4.1. PermCheck

Easy: 100
Detected time complexity: O(N) or O(N * log(N))
"""
def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
        
    seen = {key: 0 for key in range(1, len(A) + 1)}
    for a in A:
        if a in seen:
            seen[a] += 1
            if seen[a] > 1:
                return 0
        else:
            return 0
    return 1

