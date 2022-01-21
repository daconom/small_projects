from itertools import permutations

def prime(*args):
    n = len(args)
    digits=list(args)
    comb = permutations(digits, n)
    for i in list(comb):
        s = [str(j) for j in i]
        joined = int("".join(s))
        if joined > 1:
            Primenr = True
            for j in range(2, int(joined/2) + 1):
                if (joined % j) == 0:
                    Primenr = False
                    break
        if Primenr != False:
            print(joined)
                    

prime(1,3,7)
