# IDS


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


def depth_limited_search(state, goal, depth, path, visited):
    if state == goal:
        return path + [state]
    if depth == 0:
        return None
    visited.add(tuple(sorted(state.items())))
    for successor in get_successors(state):
        successor_tuple = tuple(sorted(successor.items()))

        if successor_tuple not in visited:
            result = depth_limited_search(
                successor,
                goal,
                depth - 1,
                path + [state],
                visited
            )
            if result is not None:
                return result
    return None
# ===============================
# Iterative Deepening Search
# ===============================
def iterative_deepening_search(initial_state, goal_state, max_depth=20):
    for depth in range(max_depth):
        visited = set()
        result = depth_limited_search(
            initial_state,
            goal_state,
            depth,
            [],
            visited
        )

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

    solution = iterative_deepening_search(initial_state, goal_state)

    if solution:
        print("Solution Found:\n")
        for i, step in enumerate(solution):
            print(f"Step {i}: {step}")
    else:
        print("No Solution Found")


# =========================================================
# Evaluation of IDS Algorithm
# =========================================================

# Time Complexity:
# ----------------
# O(b^d)
# b = عدد الحركات الممكنة من كل حالة
# d = عمق الحل
# Space Complexity:

# O(b * d)