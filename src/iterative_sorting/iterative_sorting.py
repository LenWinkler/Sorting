# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

           
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        

        # TO-DO: swap

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    proceed = True # flag for while loop

    while proceed == True: # keep looping while proceed is true
        
        print('looping', arr)
        for i in range(0, len(arr)):

            swap_occurred = False # var to send to while loop flag
            
            
            if i < len(arr) - 1 and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print('swap before', swap_occurred)
                swap_occurred = True
                print('swap after', swap_occurred)
                continue

            elif i < len(arr) - 1 and arr[i] < arr[i + 1]:
                print('continue')
                continue
            
            elif i == len(arr) and swap_occurred == False:
                print('len', len(arr) - 1)
                print('swap in elif', swap_occurred)
                proceed = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

    # original [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

    #          [1, 5, 4, 2, 8, 6, 0, 3, 7, 9]