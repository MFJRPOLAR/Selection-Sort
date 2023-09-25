def sort(data, first: int):
    """Sorts a listof intergers from largest to smallest 
    bypassing the elements to the left of first

    Args:
        data (int): list of integers
        first (int): the list index atwhich the sort will begin 
    """    

    #Intialize loop counter variable named i 
    i = len(data) - first - 1 

    # initialize loop counter variable named j to 0 
    j = 0 

    # Initialize variable named small that will be used 
    # to store the index of the smallest value 
    small = 0 

    # initialize varibale named temp that will be used 
    # to swap list values 
    temp = 0 

    # loop through list as many times as specified by 
    # len(data) and first 
    # this loop represents the blue arrow 
    while (i > 0 ):
        # set small equal to first
        small = first  

        # set j equal to first + 1 
        j = (first + 1)

        # loop through list starting with element at
        # first + 1 and continue until reach first + i 
        # this loop represents the yellow arrow 
        while (j <= first + i ):
            # if the value in data[small] is less than 
            # data[j]
            if (data[small] < data[j]): 
                # set small equal to j 
                small = j 
            # Increment j by 1 
            j += 1 

        # swap the data in first + i with the data in small 
        # set temp to value in data[first + i]
        temp = data[first + i]

        #set data[first+i] to value in data[small]
        data[first+i] = data[small]

        # set data[small] to value in temp
        data[small] = temp 
    
        # decrement i by 1
        i -= 1 

