# find smallest cube for which exactly 5 permutations of its digits are cube

import math

target_perms = 5
test_seed = 4800 # min 2
compute_seed = -1
cube_list = []
cube_list_index = 0


def compute_cubes():
    global compute_seed
    global test_seed
    global cube_list
    global cube_list_index
    cube_digits = len(str(test_seed ** 3))
    if len(cube_list) > 0:
        if len(str(cube_list[0])) == cube_digits:
            return
    
    print("computing cubes of length " + str(cube_digits))
    cube_list = []
    
    # calculate minimum compute seed if necessary
    # assume test seed is minimum and linear search lower values until digit cutoff is reached
    if compute_seed == -1:
        compute_seed = test_seed
        while True:
            compute_seed -= 1
            cube = compute_seed ** 3
            if len(str(cube)) < cube_digits:
                compute_seed += 1
                break
    
    cube_list_index = test_seed - compute_seed
    
    # generate cube list
    while True:
        cube = compute_seed ** 3
        if len(str(cube)) > cube_digits:
            break
        cube_list.append(cube)
        compute_seed += 1


def compute_perms(c):
    global cube_list    
    cube_perms = []
    cube_index = 0
    perms = unique_permutations(list(str(c)))
    p = int(''.join(next(perms, ['0'])))
    
    # find matches between cube list and permutations list
    while cube_index < len(cube_list):
        # match: store cube and increment both lists
        if cube_list[cube_index] == p:
            cube_perms.append(p)
            cube_index += 1
            p = int(''.join(next(perms, ['0'])))
        # cube is smaller than perm: increment cube
        elif cube_list[cube_index] < p:
            cube_index += 1
        # perm is smaller than cube: increment perm
        else:
            p = int(''.join(next(perms, ['0'])))
            
        # stop if matches exceeds target or if all permutations have been tested
        if len(cube_perms) > target_perms or p == 0:
            break
    
    # if solution is valid, return
    if len(cube_perms) == target_perms:
        print(cube_perms)
        return True
    
    # if the solution is invalid, c is not a member of the solution set; remove it
    cube_list.remove(c)
    return False


def unique_permutations(seq):
    """
    Yield only unique permutations of seq in an efficient way.

    A python implementation of Knuth's "Algorithm L", also known from the 
    std::next_permutation function of C++, and as the permutation algorithm 
    of Narayana Pandita.
    """

    # Precalculate the indices we'll be iterating over for speed
    i_indices = range(len(seq) - 1, -1, -1)
    k_indices = i_indices[1:]

    # The algorithm specifies to start with a sorted version
    seq = sorted(seq)

    while True:
        yield seq

        # Working backwards from the last-but-one index,           k
        # we find the index of the first decrease in value.  0 0 1 0 1 1 1 0
        for k in k_indices:
            if seq[k] < seq[k + 1]:
                break
        else:
            # Introducing the slightly unknown python for-else syntax:
            # else is executed only if the break statement was never reached.
            # If this is the case, seq is weakly decreasing, and we're done.
            return

        # Get item from sequence only once, for speed
        k_val = seq[k]

        # Working backwards starting with the last item,           k     i
        # find the first one greater than the one at k       0 0 1 0 1 1 1 0
        for i in i_indices:
            if k_val < seq[i]:
                break

        # Swap them in the most efficient way
        (seq[k], seq[i]) = (seq[i], seq[k])                #       k     i
                                                           # 0 0 1 1 1 1 0 0

        # Reverse the part after but not                           k
        # including k, also efficiently.                     0 0 1 1 0 0 1 1
        seq[k + 1:] = seq[-1:k:-1]
        

# Returns index of x in cube_list if present, else -1 
def binary_search(l, r, x):

    global cube_list
    
    # Check base case 
    if r >= l: 
  
        mid = math.floor(l + (r - l)/2)
        # print("L = " + str(l) + " R = " + str(r) + " mid = " + str(mid) + " x = " + str(x))
        # print(cube_list)

        # If element is present at the middle itself 
        if cube_list[mid] == x: 
            return mid
        
        # If element is smaller than mid, then it can only be present in left subarray 
        elif cube_list[mid] > x: 
            return binary_search(l, mid-1, x) 
        
        # Else the element can only be present in right subarray 
        else:
            return binary_search(mid+1, r, x)

    else: 
        # Element is not present in the array
        return -1


while True:
    # debug
    test_seed += 1
    print("seed = " + str(test_seed))
    
    # ensure all cubes with the current number of digits have been computed
    compute_cubes()
    
    # compute permutations of the next cube in the list and check for matches
    if compute_perms(cube_list[cube_list_index]):
        break
