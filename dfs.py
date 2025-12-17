# DFS

def is_clear(block, state):
    return block not in state.values()


def get_successors(state):
    successors = []
    blocks = list(state.keys())
    for block in blocks:
        if is_clear(block, state):
            if state[block] != "Table":
                new_state = state.copy()
                new_state[block] = "Table"
                successors.append(new_state)
            for target in blocks:
                if target != block and is_clear(target, state):
                    if state[block] != target:
                        new_state = state.copy()
                        new_state[block] = target
                        successors.append(new_state)
    return successors


# ===============================
# Depth First Search
# ===============================
def depth_first_search(state, goal, path, visited, max_depth=20):
    if state == goal:
        return path + [state]
    if len(path) > max_depth:
        return None

    visited.add(tuple(sorted(state.items())))
    for successor in get_successors(state):
        successor_tuple = tuple(sorted(successor.items()))
        if successor_tuple not in visited:
            result = depth_first_search(successor, goal, path + [state], visited, max_depth)
            if result is not None:
                return result
    return None


# ===============================
# Example Execution
# ===============================
if __name__ == "__main__":

    initial_state = {
        'A': 'B',
        'B': 'Table',
        'C': 'Table'
    }

    goal_state = {
        'A': 'Table',
        'B': 'A',
        'C': 'B'
    }

    visited = set()
    solution = depth_first_search(initial_state, goal_state, [], visited)

    if solution:
        print("Solution Found:\n")
        for i, step in enumerate(solution):
            print(f"Step {i}: {step}")
    else:
        print("No Solution Found")


# =========================================================
# Evaluation of DFS Algorithm
# =========================================================

# Time Complexity:
# ----------------
# O(b^d)
# b = عدد الحركات الممكنة من كل حالة
# d = عمق الشجرة (أقصى عمق للبحث)

# Space Complexity:
# -----------------
# O(b * d)