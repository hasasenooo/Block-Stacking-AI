#                           **Block Stacking Problem**



### **Overview:**



**this project implements and compares several AI Search Algorithms to solve the Block Stacking Problem — a classic planning problem in Artificial Intelligence.**

**The objective is to transform an initial configuration of stacked blocks into a target goal configuration by performing valid moves according to defined constraints.**





### **Problem Description:**



**In the Block Stacking Problem, a set of blocks (e.g., A, B, C) can be placed either on top of one another or directly on the table.**

**The goal is to rearrange the blocks from a given initial state to a goal state using valid moves.**



##### **Example:**



###### **Initial State:**

**A on B, B on table, C on table**



###### **Goal State:**

**C on B, B on A**



### **Rules and Constraints:**



**Only one block can be moved at a time.**



**A block can be moved only if it has no block on top of it (i.e., it’s clear).**



**Blocks can be placed on top of another clear block or on the table.**



**Each move has a uniform cost of 1.**





##### **Search Algorithms Overview:**



**The following search algorithms will be implemented and compared for solving the problem:**



###### **1. Breadth-First Search (BFS):**



**BFS explores the search space \*\*level by level\*\*, starting from the initial state and expanding all nodes at the current depth before moving to the next depth.**  

**It guarantees the shortest path to the goal but can consume a lot of memory for large problems.**



###### **2. Depth-First Search (DFS):**



**DFS explores the search space by \*\*going as deep as possible\*\* along one branch before backtracking.**  

**It is memory-efficient but may not find the optimal solution because it can get stuck in deep but non-optimal paths.**



###### **3. Uniform Cost Search (UCS):**



**UCS expands nodes based on the \*\*cost of reaching them\*\*, always selecting the node with the lowest cumulative cost.**  

**It guarantees an optimal solution when all moves have uniform or varying costs.**



###### **4. Iterative Deepening Search (IDS):**



**IDS combines the benefits of DFS and BFS.**  

**It performs DFS with increasing depth limits until the goal is found, providing \*\*optimality\*\* like BFS while using less memory.**



###### **A\* Search:**



**A\* is an \*\*informed search algorithm\*\* that uses a \*\*heuristic function\*\* to estimate the cost from a node to the goal.**  

**It explores the most promising paths first, usually solving problems faster than uninformed search algorithms.**

