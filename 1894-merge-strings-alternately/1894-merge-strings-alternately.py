class Solution:
    def mergeAlternately(self, word1, word2):
        lenW1 = len(word1)
        lenW2 = len(word2)

        i = 0
        j = 0
        result=[]

        while i<lenW1 or j<lenW2:
            if i<lenW1:
                result.append(word1[i])
                i+=1
            if j<lenW2:
                result.append(word2[j])
                j+=1
        return "".join(result)

solution = Solution()
word1 = "abc"
word2 = "xyz"
merge = solution.mergeAlternately(word1,word2)
print(merge)