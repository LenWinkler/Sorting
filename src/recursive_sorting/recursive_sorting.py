# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    for i in range(0, elements):

    # check if either arr is empty
    # if one arr is empty, add first element from non empty arr to merged_arr
        
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB = arrB[1:]
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            arrA = arrA[1:]
            
    # otherwise, compare first element of each arr
        elif arrA[0] < arrB[0]:
            # insert larger element into merged_arr
            merged_arr[i] = arrA[0]
             # remove element from original arr
            arrA.pop(0)
        else:
            # insert larger element into merged_arr
            merged_arr[i] = arrB[0]
             # remove element from original arr
            arrB.pop(0)
    
   
    # continue until both original arrs are empty
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    
    if len(arr) > 1:
        # divide into left and right
        left = merge_sort( arr[ 0 : len(arr) // 2 ] )
        right = merge_sort( arr[ len(arr) // 2 : ] )
        # merge sorted lists
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
