T = int(input())
for i in range(1, T + 1):
    N = int(input())
    lydia = input()
    steps = lydia.replace('E', 'X')
    steps = steps.replace('S', 'E')
    steps = steps.replace('X', 'S')

    print('Case #{}: {}'.format(i, steps))
