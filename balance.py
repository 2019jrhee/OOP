
def balance(left, right):
    # store weights of arguments
    left_weight = 0
    right_weight = 0
    # check weight of each argument
    for x in left:
        if x == '!':
            left_weight = left_weight + 2
        else: left_weight = left_weight +3

    for y in right:
        if y == '!':
            right_weight = right_weight + 2
        else: right_weight = right_weight + 3

    if (left_weight > right_weight):
        print ('left')
    elif (right_weight > left_weight):
        print ('right')
    else:
        print ('balance')

    print (left_weight)
    print (right_weight)

balance ('!!','??')
