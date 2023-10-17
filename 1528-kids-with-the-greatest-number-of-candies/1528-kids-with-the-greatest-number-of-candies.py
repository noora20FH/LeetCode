from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies among all kids
        max_candies = max(candies)
        
        # Initialize a list to store the results
        result = []
        
        # Check each kid's candies after adding extraCandies
        for kid_candies in candies:
            if kid_candies + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result

# Example usage:
solution = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = solution.kidsWithCandies(candies, extraCandies)
print(result)  # Output: [True, True, True, False, True]

        