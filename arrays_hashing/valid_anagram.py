class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        for i in s:
            s_list.append(i)
        for j in t:
            t_list.append(j)
        s_list.sort()
        t_list.sort()
        return s_list == t_list
    
# Case 1
s="racecar"
t="carrace"
print(Solution().isAnagram(s, t)) # True

s="jar"
t="jam"
print(Solution().isAnagram(s, t)) # False

s="dormitory"
t="dirtyroom"
print(Solution().isAnagram(s, t)) # True

# Time complexity: O(nlogn) where n is the length of the string
# Check length
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
