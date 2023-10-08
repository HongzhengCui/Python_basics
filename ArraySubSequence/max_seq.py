def max_seq(l):
    """
    max_seq returns a the maximum increasing contiguous subsequence in the list.
    (as determined by length).  If two or more subsequences have equal lengths,
    return the first subsequence found.
   
    Args:
    l(list): list of numbers

    Returns:
    the maximum increasing contiguous subsequence as a list. If the l is empty,
    an empty list is returned

    Raises:
    TypeError if the list contains an item that is not arithmetically 
    compatible with ints and floats
    """
    str_num = 0
    for i in range(len(l)):
        if type(l[i]) is int or type(l[i]) is float:
            str_num = str_num + 1
    
    if str_num == 0:
        if l == []:
            max_seq = []
        else:
            raise TypeError("All elements in the list must be int or float")
    
    pointers = []
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            pointers.append(i)
    
    if pointers == []:
        max_seq = l
        
    else:
        seq = []
        subseq = []
        for x in range(len(pointers)):
            if x == 0:
                for y in range(len(l)):
                    if y <= pointers[x]:
                        subseq.append(l[y])
                seq.append(subseq)
                subseq = []
            
            else:
                for y in range(len(l)):
                    if y <= pointers[x] and y > pointers[x-1]:
                        subseq.append(l[y])
                seq.append(subseq)
                subseq = []
            
        for y in range(len(l)):
            if y > pointers[-1]:
                subseq.append(l[y])
        seq.append(subseq)
    
        max_len = 0
        for subseq in seq:
            if len(subseq) > max_len:
                max_len = len(subseq)
                max_seq = subseq
    
    return max_seq