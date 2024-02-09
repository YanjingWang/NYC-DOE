class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.leader = []
        self.times = times
        leader, count = -1, {}

        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(leader, 0):
                leader = p
            self.leader.append(leader)
       

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        left, right = 0, len(self.times) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] == t:
                return self.leader[mid]
            elif self.times[mid] < t:
                left = mid + 1
            else:
                right = mid - 1
        return self.leader[right]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
    
if __name__ == '__main__':
    persons = [0,1,1,0,0,1,0]
    times = [0,5,10,15,20,25,30]
    obj = TopVotedCandidate(persons, times)
    print(obj.q(3))
    print(obj.q(12))
    print(obj.q(25))
    print(obj.q(15))
    print(obj.q(24))
    print(obj.q(8))