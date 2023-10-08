def compute_average(l):
    """
    Computes the average of list, ignoring any entries that 
    are not numbers (floats or ints)

    Args:
    l(list): list of items to compute the average
 
    returns:
    average of the numbers in the list
    
    raises:
    ValueError if the argument is not a list or if the list does not contain any numbers
    """
    # TODO: Implement function
    num = []
    avg = 0
    if type(l) is not list:
        raise ValueError("The input is not a list.")
        
    elif len(l) == 0:
        raise ValueError("The list is empty.")
        
    else:
        for i in l:
            if type(i) is int or type(i) is float:
                num.append(i)
                
        if len(num) == 0:
            raise ValueError("The list does not contain any ints or floats.")
           
        else:
            avg = sum(num) / len(num)    
            return avg
