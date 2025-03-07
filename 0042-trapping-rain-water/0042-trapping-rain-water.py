from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: If height is empty or too short to trap water
        if not height or len(height) < 3:
            return 0  # No trapped water possible

        # Initialize two pointers
        left, right = 0, len(height) - 1  
        
        # Track the maximum height seen from both sides
        left_max, right_max = height[left], height[right]  
        
        # Variable to store total trapped water
        trapped_water = 0  

        # Process until the two pointers meet
        while left < right:
            # The side with the smaller max height is the limiting factor
            if left_max < right_max:
                left += 1  # Move left pointer to the right
                left_max = max(left_max, height[left])  # Update left_max if needed
                trapped_water += max(0, left_max - height[left])  # Add trapped water at this index
            else:
                right -= 1  # Move right pointer to the left
                right_max = max(right_max, height[right])  # Update right_max if needed
                trapped_water += max(0, right_max - height[right])  # Add trapped water at this index

        # Return total trapped water
        return trapped_water
