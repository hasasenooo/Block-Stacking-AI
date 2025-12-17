# UCS (Uniform Cost Search)

import heapq


def is_clear(block, state):
    return block not in state.values()


def get_successors(state):
    successors = []
    blocks = list(state.keys())
    for block in blocks:
        if is_clear(block, state):
            # Move block to the table
            if state[block] != "Table":
                new_state = state.copy()
                new_state[block] = "Table"
                successors.append((new_state, 1))  # cost = 1

            # Move block onto another clear block
            for target in blocks:
                if target != block and is_clear(target, state):
                    if state[block] != target:
                        new_state = state.copy()
                        new_state[block] = target
                        successors.append((new_state, 1))  # cost = 1
    return successors


# ===============================
# Uniform Cost Search
# ===============================
def uniform_cost_search(initial_state, goal_state):
    frontier = []
    heapq.heappush(frontier, (0, [initial_state]))  # (cost, path)
    visited = set()

    while frontier:
        cost, path = heapq.heappop(frontier)
        state = path[-1]

        if state == goal_state:
            return path

        state_tuple = tuple(sorted(state.items()))
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for successor, step_cost in get_successors(state):
            successor_tuple = tuple(sorted(successor.items()))
            if successor_tuple not in visited:
                heapq.heappush(frontier, (cost + step_cost, path + [successor]))

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

    solution = uniform_cost_search(initial_state, goal_state)

    if solution:
        print("Solution Found:\n")
        for i, step in enumerate(solution):
            print(f"Step {i}: {step}")
    else:
        print("No Solution Found")


# =========================================================
# Evaluation of UCS Algorithm
# =========================================================

# Time Complexity:
# ----------------
# O(b^(1 + ⌈C*/ε⌉))
# حيث:
# b = عدد الفروع (الحركات الممكنة من كل حالة)
# C* = تكلفة أقل مسار للحل
# ε = أقل تكلفة خطوة (هنا = 1)

# Space Complexity:
# -----------------
# O(b^(1 + ⌈C*/ε⌉))
# لأن UCS يخزن كل الحالات في الـ frontier بترتيب التكلفة.