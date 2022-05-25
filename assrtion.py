def modulus_three(n):
    r = n%3
    if r == 0:
        print("multiple of 3")
    elif r ==1:
        print("remainder 1")
    else:
        assert r ==2, "Remainder is not 2"
        print("remainder 2")