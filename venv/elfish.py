def is_x_ish(base, test):
    """ takes a string and returns true if the letters of base are in test

    ex: is_x_ish("elf", "leaf") >>> true
    ex: is_x_ish("red", "rover") >>> false

    take each letter in base and test against each letter in test
    if it isn't found, then return false
    otherwise go to next letter until all letter are found


    """
    assert len(base) != 0 and test != 0, "Base and test must not be empty"
    test_letter = base[0]
    k = 0
    while k < len(test):
        if test_letter == test[k]:
            if len(base) == 1:
                return True
            elif is_x_ish(base[1:len(base)], test):
                return True
            else:
                return False
        else:
            k += 1
    return False


print(is_x_ish("dem", "dream"))
