class Solution:
    def reverseWords(self, s: str) -> str:
       
        # Split the input string into words using whitespace as the separator
        words = s.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words into a string with a single space separator
        reversed_string = " ".join(reversed_words)
        
        return reversed_string

# Example usage:
solution = Solution()
input_string = "the sky is blue"
output_string = solution.reverseWords(input_string)
print(output_string)  # Output: "blue is sky the"
