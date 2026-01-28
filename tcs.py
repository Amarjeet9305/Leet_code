from collections import deque

# Check if the ladder cells are valid (inside grid and not blocked)
def is_valid(pos_list, grid, M, N):
    for r, c in pos_list:
        if not (0 <= r < M and 0 <= c < N):
            return False
        if grid[r][c] == 'B':
            return False
    return True

# Get all the cells occupied by the ladder for given position and orientation
def get_ladder_cells(r, c, length, orientation):
    if orientation == 'H':
        return [(r, c + i) for i in range(length)]
    else:
        return [(r + i, c) for i in range(length)]

# Check if all the cells in the ladder's square area are empty to rotate
def can_rotate(r, c, length, grid, M, N):
    half = length // 2
    for i in range(-half, half + 1):
        for j in range(-half, half + 1):
            nr, nc = r + i, c + j
            if not (0 <= nr < M and 0 <= nc < N):
                return False
            if grid[nr][nc] == 'B':
                return False
    return True

def find_ladder_ends(grid, M, N, char):
    coords = [(r, c) for r in range(M) for c in range(N) if grid[r][c] == char]
    coords.sort()
    return coords

def ladder_problem(grid, M, N):
    # Identify source and destination ladder positions
    source_cells = find_ladder_ends(grid, M, N, 'l')
    dest_cells = find_ladder_ends(grid, M, N, 'L')

    if not source_cells or not dest_cells:
        return "Impossible"

    length = len(source_cells)
    sr, sc = source_cells[0]
    dr, dc = dest_cells[0]

    # Determine initial orientation
    orientation = 'H' if source_cells[0][0] == source_cells[1][0] else 'V'
    dest_orientation = 'H' if dest_cells[0][0] == dest_cells[1][0] else 'V'

    q = deque()
    q.append((sr, sc, orientation, 0))
    visited = set()
    visited.add((sr, sc, orientation))

    while q:
        r, c, orient, steps = q.popleft()

        # Check if destination reached
        if orient == dest_orientation:
            if set(get_ladder_cells(r, c, length, orient)) == set(dest_cells):
                return steps

        # Try moving in 4 directions
        for dr_move, dc_move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr_move, c + dc_move
            new_cells = get_ladder_cells(nr, nc, length, orient)
            if is_valid(new_cells, grid, M, N) and (nr, nc, orient) not in visited:
                visited.add((nr, nc, orient))
                q.append((nr, nc, orient, steps + 1))

        # Try rotating
        if can_rotate(r, c, length, grid, M, N):
            new_orient = 'V' if orient == 'H' else 'H'
            new_cells = get_ladder_cells(r, c, length, new_orient)
            if is_valid(new_cells, grid, M, N) and (r, c, new_orient) not in visited:
                visited.add((r, c, new_orient))
                q.append((r, c, new_orient, steps + 1))

    return "Impossible"


# ---------- MAIN ----------
if __name__ == "__main__":
    M, N = map(int, input().split())
    grid = [list(input().strip()) for _ in range(M)]
    print(ladder_problem(grid, M, N))
