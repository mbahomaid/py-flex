def sum_of_two(nums, target):
    """
    Finds two numbers in the list `nums` that add up to `target`.
    
    :param nums: List of integers
    :param target: Target sum
    :return: Indices of the two numbers that add up to the target
    """
    # Dictionary to store the difference between target and each number
    num_map = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement (number needed to reach the target)
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_map:
            return [num_map[complement], i]  # Return the indices
        
        # Store the current number and its index in the dictionary
        num_map[num] = i
    
    # If no solution is found, return an empty list
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(sum_of_two(nums, target))  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
