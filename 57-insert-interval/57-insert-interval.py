class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        output = []
        
        for i in range(len(intervals)):
            if new[1] < intervals[i][0]:
                output.append(new)
                return output + intervals[i:]
            elif new[0] > intervals[i][1]:
                output.append(intervals[i])
                
            else:
                new = [min(new[0],intervals[i][0]),max(new[1],intervals[i][1])]
        output.append(new)
        return output 