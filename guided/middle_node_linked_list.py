def find_middle_node_linked_list(ll):
    # IDEA 1
    # get length of ll
    # traverse ll a keep counter to count how long the ll is
    # calculate midpoint
    # use midpoint formula from binary search
    # start form head of ll, jump until we reach midpoint node

    # IDEA 2
    # have two pointers that start at beginning
    f = ll
    s = ll
    # one runs at twice the speed of the other
    # how do we move it at twice the speed?
    # set fast = fast.next.next
    # while fast has not reached end of list
    while f and f.next:
        f = f.next.next
        s = s.next
    # once the faster pointer reaches end of track, the slower pointer will be at the middle node
    # return slower pointer's node
    return slow
