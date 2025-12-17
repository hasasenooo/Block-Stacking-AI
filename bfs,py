import copy

def is_goal(current_state, goal_state):
    return sorted(current_state) == sorted(goal_state)

def get_possible_moves(state):
    moves = []
    for i, stack in enumerate(state):
        if not stack: continue
        
        for j in range(len(state)):
            if i == j: continue
            new_state = copy.deepcopy(state)
            block = new_state[i].pop()
            new_state[j].append(block)
            new_state = [s for s in new_state if s]
            moves.append(new_state)
            
        if len(stack) > 1:
            new_state = copy.deepcopy(state)
            block = new_state[i].pop()
            new_state.append([block])
            moves.append(new_state)
            
    return moves

def dfs(current_state, goal_state, visited, path):
    state_tuple = tuple(sorted([tuple(s) for s in current_state]))
    
    if state_tuple in visited:
        return None
    
    visited.add(state_tuple)
    path.append(current_state)

    if is_goal(current_state, goal_state):
        return path

    for next_state in get_possible_moves(current_state):
        result = dfs(next_state, goal_state, visited, path[:])
        if result:
            return result
            
    return None
start_node = [['A', 'B', 'C']]
goal_node = [['A'], ['B', 'C']]

solution = dfs(start_node, goal_node, set(), [])

if solution:
    print("The solution has been found:")
    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")
else:
    print("No solution was found.")