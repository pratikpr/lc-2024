# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    
    result = []
    
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
            
    return result

        
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))

intervals = [[1,4],[4,5]]
print(merge(intervals))