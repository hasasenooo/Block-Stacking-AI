# A*

import heapq
import itertools

counter = itertools.count() 


def is_clear(block, state):
    # لو مفيش بلوك فوقه هيعتبر clear
    return block not in state.values()


def get_successors(state):
    # كل الحالات الممكنه
    successors = []
    blocks = list(state.keys())

    for block in blocks:
        if is_clear(block, state):

            # تحريك البلوك إلى الترابيزة
            if state[block] != "Table":
                new_state = state.copy()
                new_state[block] = "Table"
                successors.append(new_state)

            # تحريك البلوك فوق بلوك تاني clear
            for target in blocks:
                if target != block and is_clear(target, state):
                    if state[block] != target:
                        new_state = state.copy()
                        new_state[block] = target
                        successors.append(new_state)

    return successors


def heuristic(state, goal):
    # Heuristic :
    # عدد البلوكات اللي مش في مكانها
    misplaced = 0
    for block in state:
        if state[block] != goal[block]:
            misplaced += 1
    return misplaced


def a_star(initial_state, goal_state):

    # A*
    open_list = []
    closed_set = set()

    # إضافة الحالة الابتدائية
    heapq.heappush(
        open_list,
        (
            heuristic(initial_state, goal_state),
            next(counter),   
            0,
            initial_state,
            []
        )
    )

    while open_list:
        f, _, g, current_state, path = heapq.heappop(open_list)

        state_tuple = tuple(sorted(current_state.items()))

        # التحقق من الوصول للهدف
        if current_state == goal_state:
            return path + [current_state]

        if state_tuple in closed_set:
            continue

        closed_set.add(state_tuple)

        for successor in get_successors(current_state):
            successor_tuple = tuple(sorted(successor.items()))

            if successor_tuple not in closed_set:
                new_g = g + 1
                new_h = heuristic(successor, goal_state)
                new_f = new_g + new_h

                heapq.heappush(
                    open_list,
                    (
                        new_f,
                        next(counter),  
                        new_g,
                        successor,
                        path + [current_state]
                    )
                )

    return None


# تجربه
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

    solution = a_star(initial_state, goal_state)

    if solution:
        print("Solution Found:\n")
        for i, step in enumerate(solution):
            print(f"Step {i}: {step}")
    else:
        print("No Solution Found")


# Evaluation
 
#Time Complexity:
#O(b^d)
#b = عدد الحالات الممكنة 
#d = عمق الحل (عدد الحركات للوصول للهدف)

#Space Complexity:
#O(b^d)
#A* بتاخد مساحه كبيره