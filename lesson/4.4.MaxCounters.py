"""
1. MaxCounters
Calculate the values of counters after applying all alternating operations: 
increase counter by 1; set value of all counters to current maximum.

Medium: 100

"""
def solution(N, A):
    # write your code in Python 3.6
    
    if len(A) == 0:
        return []
        
    counters = {key + 1: 0 for key in range(N)}
    
    tmp_Max, Max = 0, 0
    for a in A:
        if a < N + 1:
            if counters[a] <= Max:
                counters[a] = Max + 1
            else:
                counters[a] += 1
                
            if counters[a] > tmp_Max:
                tmp_Max = counters[a]
        else:
            Max = tmp_Max

    for c in counters:
        if counters[c] <= Max:
            counters[c] = Max
    
    return list(counters.values())