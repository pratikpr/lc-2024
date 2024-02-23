# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

def canCompleteCircuit(gas, cost) -> int:
    total_diff = 0
    curr_gain = 0
    answer = 0
    
    for i in range(len(gas)):
        total_diff += gas[i] - cost[i]
        curr_gain += gas[i] - cost[i]
        
        if curr_gain < 0:
            curr_gain = 0
            answer = i+1
            
    return answer if total_diff >= 0 else -1


gas = [1,2,3,4,5]; cost = [3,4,5,1,2]
print(canCompleteCircuit(gas, cost))

gas = [2,3,4]; cost = [3,4,3]
print(canCompleteCircuit(gas, cost))
