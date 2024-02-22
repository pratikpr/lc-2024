# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

def canAttendMeetings(intervals) -> bool:
    intervals.sort(key = lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

intervals = [[0,30],[5,10],[15,20]]
print(canAttendMeetings(intervals))

intervals = [[7,10],[2,4]]
print(canAttendMeetings(intervals))