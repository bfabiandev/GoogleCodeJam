import math

def merge_overlaps(intervals):
    intervals.sort(key=lambda x: x[0])
    done = False
    while not done:
        done = True
        for idx in range(len(intervals) - 1):
            if intervals[idx][1] > intervals[idx + 1][0]:
                new_interval = (min(intervals[idx][0], intervals[idx+1][0]), max(intervals[idx][1], intervals[idx+1][1]))
                del intervals[idx+1]
                del intervals[idx]
                intervals.append(new_interval)
                intervals.sort(key=lambda x: x[0])
                done = False
                break
    
    return intervals


T = int(input())
for i in range(1, T+1):
    [N, P_original] = [int(s) for s in input().split()]
    cookies = []
    for _ in range(N):
        cookies.append([int(s) for s in input().split()])
    
    P = P_original
    cookie_limits = []
    for c in cookies:
        W, H = c
        diameter = 2 * (W + H)
        P -= diameter
        mini = 2 * min(W, H)
        maxi = 2 * math.sqrt(W*W + H*H)
        cookie_limits.append((mini, maxi))

    sum_diameters = P_original - P

    intervals = [(0, 0)]
    for l in cookie_limits:
        mini, maxi = l
        new = [(mini+L, maxi+R) for (L, R) in intervals]
        intervals.extend(new)
        intervals = merge_overlaps(intervals)
    
    best = sum_diameters
    done = False
    for (L, R) in intervals:
        if P >= L and P <= R:
            print("Case #{}: {}".format(i, float(P_original)))
            done = True
            break
        elif P < L:
            print("Case #{}: {}".format(i, best))
            done = True
            break
        elif P > R:
            best = sum_diameters + R
        else:
            pass
    
    if not done:
        print("Case #{}: {}".format(i, best))
    
