T = int(input())
for i in range(1, T + 1):
    [B, M] = [int(i) for i in input().split()]
    if M > 2**(B-2):
        result = "IMPOSSIBLE"
        print("Case #{}: {}".format(i, result))
    else:
        result = "POSSIBLE"
        print("Case #{}: {}".format(i, result))
        if B > 2:
            binary = "{0:b}".format(M-1).zfill(B-2)
        else:
            binary = ""
        print("0" + binary + "1")
        for j in range(1, B):
            print((j+1)*"0" + (B-j-1)*"1")
