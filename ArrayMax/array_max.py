def array_max(array):
    """
    Finds the largest number in the list.
    Ignores elements that are not an int or a float

    Args:
        array (list): list of numbers (either float or int)

    Returns:
    Largest number in the list.  None if array is empty
    or if array is not a list.
    """
    if isinstance(array, list) == False or len(array) == 0:
        max = None
    
    else:
        nums = []
        max = 0
        for item in array:
            if isinstance(item, (int, float)):
                nums.append(item)
            
        if len(nums) == 0:
            max = None
        else:
            max = nums[0]
            for i in range(len(nums)-1):
                if nums[i+1] >= max:
                    max = nums[i+1]
    return max     
    

