#  Nathan Zhu  Sunday 8:03 pm, Chiago O'Hare airport when airplane got delayed.
#  Leetcode 75 | medium | I think tricky AF, esp during interview


def dutch_flag(arr):
    # red, white, blue point to the last index of red/white/blue
    # for this last index, we don't know the actual color, but
    # the invariant is that the index before should be sorted.
    # 
    # Ex. index before index at red, index - 1 should be red
    # There are cases in which this is not true, for example
    # at the very beginning when red and white point to the beginning
    # of the array.  Also, is false when there is none of a color seen yet.
    #
    # NOTE: Red >= white at all times
    # 
    red, white, blue = 0, 0, len(arr) - 1

    while white <= blue:
        # We reveal the arr[white] to point to a red color
        # So, let's first agree that either red is either pointing
        # to a red element or a white element.  This is true because
        # white >= red, and if white finds a blue, it swaps blue to the end.
        # I also *THINK* when red > white, red must be pointing to a white
        # at all times, but I'm not 100% sure.
        #
        # Ok, so the first step is straightforward. 
        #
        # Suppose red is pointing to a 1 and white to a 0
        # Ex. 0 1 0 ?
        #       R W
        # We swap and increment R & W
        #     0 0 1 ?
        #         R W
        # Ex. 1 1 0 ?
        #     R   W
        #     0 1 1 ? 
        #       R   W
        # Obviously red's boundary increasing by 1, so red should increase by 1.
        # However, I believe that barring one case, white's boundary increases by 1
        #
        # Assuming red != white (this means white > red), we know red must be pointing
        # to a white.  This is because red CANNOT point to a blue, as otherwise it would've
        # been swapped to the right earlier by the white pointer.  The red CANNOT point
        # to a red, as otherwise it would've been swapped over, I THINK.  *not 100% sure*
        # If this is true, white's boundary must increase by 1.  If it is true that a 
        # white is always swapped over, if we take out the white += 1, this algo should still
        # work.  NOTE: I was wrong, it is not optional. 
        #
        # The other case, when red == white, is we swap it with itself (doing nothing), 
        # and increment both pointers.
        #
        if arr[white] == 0:
            arr[red], arr[white] = arr[white], arr[red]
            red += 1
            white += 1  # this line is NOT optional #
        # We add a white to the boundary
        if arr[white] == 1:
            white += 1
        # So, we have no idea what blue is pointing to. It can be everything from a 
        # red white or blue. But we do know we are swapping a blue over.  So, we decrement
        # blue's boundary, but do nothing for white's boundary.
        if arr[white] == 2:
            arr[white], arr[blue] = arr[blue], arr[white]
            blue -= 1
