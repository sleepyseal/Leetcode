class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort()
        print(people)
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(Solution().reconstructQueue(people))