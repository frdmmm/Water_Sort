from collections import deque

def is_goal_state(state):
    a = []
    for bottle in state:
        if len(bottle) > 0:
            a.append(bottle[0])
            if len(set(bottle)) > 1:
                return False
    if len(set(a))!=len(a):
        return False
    return True

def get_valid_moves(state, tube_capacity):
    moves = []
    n = len(state)
    for i in range(n):
        if len(state[i]) == 0:
            continue
        for j in range(n):
            if i != j and (len(state[j]) == 0 or (len(state[j]) < tube_capacity and state[j][-1] == state[i][-1])):
                moves.append((i, j))
    return moves

def apply_move(state, move):
    new_state = [list(bottle) for bottle in state]
    from_bottle, to_bottle = move
    liquid = new_state[from_bottle].pop()
    new_state[to_bottle].append(liquid)
    return tuple(tuple(bottle) for bottle in new_state)

def water_sort_solver(initial_state, tube_capacity):
    initial_state = tuple(tuple(bottle) for bottle in initial_state)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        
        if is_goal_state(current_state):
            print("Keadaan final:", current_state)
            return path
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        
        for move in get_valid_moves(current_state, tube_capacity):
            next_state = apply_move(current_state, move)
            if next_state not in visited:
                queue.append((next_state, path + [move]))
    return None

# initial_state = [
#     [1, 2, 3, 4],
#     [5, 6, 1, 1],
#     [7, 8, 1, 5],
#     [2, 9, 10, 10],
#     [9, 11, 7, 5],
#     [12, 6, 9, 8],
#     [11, 9, 11, 2],
#     [2, 3, 6, 12],
#     [10, 8, 12, 6],
#     [8, 12, 4, 5],
#     [4, 11, 3, 3],
#     [7, 7, 10, 4],
#     [],
#     []
# ]

initial_state = [
    [1, 2, 2, 1],
    [3, 1, 4, 2],
    [4, 5, 3, 2],
    [5, 1, 3, 2],
    [4, 5, 3, 1],
    [],
    []
]

tube_capacity = 5

solution = water_sort_solver(initial_state, tube_capacity)
if solution:
    print("Solution found:")
    for move in solution:
        print(f"Move liquid from bottle {move[0]} to bottle {move[1]}")
else:
    print("No solution found")
