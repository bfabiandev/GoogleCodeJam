import random


def is_valid(source, target):
    if not source:
        return True
    if source[0] == target[0] or source[1] == target[1] or source[0] + source[1] == target[0] + target[1] \
            or source[0] - source[1] == target[0] - target[1]:
        return False
    return True


def solve(available_tiles, selected_tiles):
    if len(available_tiles) == 0:
        return []

    prev_tile = selected_tiles[-1] if len(selected_tiles) > 0 else None

    for tile in available_tiles:
        if is_valid(prev_tile, tile):
            new_selected_tiles = selected_tiles.copy()
            new_available_tiles = available_tiles.copy()
            new_selected_tiles.append(tile)
            new_available_tiles.remove(tile)
            solution_from_here = solve(new_available_tiles, new_selected_tiles)
            if solution_from_here is None:
                continue
            return [tile] + solution_from_here
    return None


T = int(input())

for i in range(1, T + 1):
    R, C = [int(k) for k in input().strip().split(' ')]

    available_tiles = [(r, c) for r in range(1, R + 1) for c in range(1, C + 1)]
    random.shuffle(available_tiles)

    selected_tiles = []

    solution = solve(available_tiles, selected_tiles)
    if not solution:
        print('Case #{}: {}'.format(i, 'IMPOSSIBLE'))
    else:
        print('Case #{}: {}'.format(i, 'POSSIBLE'))
        for tile in solution:
            print('{} {}'.format(tile[0], tile[1]))
