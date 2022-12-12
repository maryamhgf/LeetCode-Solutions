class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        def find_changing_interval(intervals, newInterval):
            new_start = newInterval[0]
            indx = 0
            while(indx < len(intervals) and intervals[indx][0] < new_start):
                indx += 1
            if(indx != 0):
                indx -= 1
            return indx
            
        def merging(interval1, interval2):
            if(interval1[0] <= interval2[0] and interval1[1] >= interval2[0]):
                return [interval1[0], max(interval1[1], interval2[1])]
            return None

        def check_mergining(intervals, prev_indx):
            i = prev_indx
            while i < len(intervals) - 1:
                merged = merging(intervals[i], intervals[i+1])
                if(merged != None):
                    intervals[i+1] = merged
                    intervals.pop(i)
                else: 
                    i = i + 1
            return intervals

        def apply_changes_intervals(intervals, new_interval, prev_idx, post_idx):
            if intervals[prev_idx][1] < new_interval[0] and  new_interval[1] < intervals[post_idx][0]:
                return intervals[0: prev_idx+ 1].append(new_interval) +intervals[post_idx:]
            if new_interval[1] < intervals[post_idx][0]:
                intervals[prev_idx] = new_interval
                return intervals
            if new_interval[0] < intervals[post_idx][0]:
                intervals[post_idx] = new_interval
                return intervals         


        new_start = newInterval[0]
        new_end = newInterval[1]
        if(len(intervals) == 0):
            return [newInterval]
        indx_chaning_interval = find_changing_interval(intervals, newInterval)
        prev_interval_start = intervals[indx_chaning_interval][0]
        prev_interval_end = intervals[indx_chaning_interval][1]
        if(indx_chaning_interval != len(intervals)-1):
            post_interval_start = intervals[indx_chaning_interval+1][0]
            post_interval_end = intervals[indx_chaning_interval+1][1]
        if prev_interval_end <= new_start and new_end <= post_interval_start:
            new_interval_start = new_start
            new_interval_end = new_end
        elif prev_interval_start <= new_start and new_end <= post_interval_start:
            new_interval_start = prev_interval_start
            new_interval_end = max(new_end, prev_interval_end)
        elif prev_interval_end <= new_start:
            new_interval_start = new_start
            new_interval_end = max(new_end, post_interval_end)
        elif post_interval_start <= new_start:
            new_interval_start = post_interval_start
            new_interval_end = max(new_end, post_interval_end)
        else:
            new_interval_start = min(prev_interval_start, new_start)
            new_interval_end = max(new_end, post_interval_end)
        new_intervals = apply_changes_intervals(intervals, [new_interval_start, new_interval_end], indx_chaning_interval,               indx_chaning_interval + 1)
        return check_mergining(new_intervals, indx_chaning_interval)
