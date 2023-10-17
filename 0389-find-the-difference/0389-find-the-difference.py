class Solution:
    def findTheDifference(self, s, t):
        givingVal = {}

        for char in s: 
            givingVal[char] = givingVal.get(char,0)+1
        
        for char in t:
            if char in givingVal and givingVal[char]>0:
                givingVal[char]-=1
            else:
                return char

solution = Solution()
s = "abcd"
t = "abecd"
findDiff = solution.findTheDifference(s,t)
print(findDiff)
        