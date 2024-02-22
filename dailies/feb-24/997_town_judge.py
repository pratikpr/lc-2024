# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

def findJudge(n: int, trust) -> int:
    trusts, trusted_by = [0] * (n+1), [0] * (n+1)
    
    for pair in trust:
        trusts[pair[0]] += 1 
        trusted_by[pair[1]] += 1
      
    for i in range(1, n+1):
        if  trusts[i] == 0 and trusted_by[i] == n-1:
            return i
        
    return -1

def findJudgeFaster(n, trust):
    trust_score = [0] * (n+1)
    
    for pair in trust:
        trust_score[pair[0]] -= 1
        trust_score[pair[1]] += 1
        
    for i in range(1, n+1):
        if trust_score[i] == n-1:
            return i
        
    return -1

n = 2; trust = [[1,2]]
print(findJudgeFaster(n, trust))

n = 3; trust = [[1,3],[2,3],[3,1]]
print(findJudgeFaster(n, trust))

n = 3; trust = [[1,3],[2,3]]
print(findJudgeFaster(n, trust))