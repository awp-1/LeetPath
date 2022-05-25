class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        output = [intervals[0]]
        for start,end in intervals[1:]:
            last = output[-1][1]
            
            if start <= last:
                output[-1][1] = max(end,last)
            else:
                output.append([start,end])
        return output