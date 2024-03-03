# We are given a list schedule of employees, which represents the working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
        

class Solution:
    def employeeFreeTime(schedule: '[[Interval]]') -> '[Interval]':
        
        # merge all time intervals
        intervals = []
        for interval in schedule:
            for int in interval:
                intervals.append(int)
        
        intervals.sort(key=lambda x: x.start)
        
        merged = []
        for interval in intervals:
            if not merged or interval.start > merged[-1].end:
                merged.append(interval)
            else:
                merged[-1].end = max(interval.end, merged[-1].end)
                
        free = []
        for i in range(1, len(merged)):
            free.append(Interval(start=merged[i-1].end, end=merged[i].start))
        return free
        
        