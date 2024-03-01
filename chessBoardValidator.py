def isValidChessBoard(dictionary):
    valid = True
    bcount, wcount, bking, wking, bpawn, wpawn = 0, 0, 0, 0, 0, 0
    validKeys = ['1', '2', '3', '4', '5', '6', '7', '8', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for v in dictionary.values():
        # count num of kings
        if v == 'bking':
            bking = bking + 1
        elif v == 'wking':
            wking = wking + 1
        # count num of black and white pcs
        if v.startswith('b'):
            bcount = bcount + 1
        elif v.startswith('w'):
            wcount = wcount + 1
        # count number of pawns
        if v == 'bpawn':
            bpawn += 1
        elif v == 'wpawn':
            wpawn += 1
    
    for k in dictionary.keys():
        if k[0] not in validKeys:
            valid = False
        if k[1] not in validKeys:
            valid = False
    
    # is there exactly one white king and one black king?
    if (bking or wking) != 1:
        valid = False
    # is there at most 16 pcs per player?
    if (bcount or wcount) > 16:
        valid = False
    # is there at most 8 pawns per player?
    if (bpawn or wpawn) > 8:
        valid = False
    
    return valid

print(str(isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'})))