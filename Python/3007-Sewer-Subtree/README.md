A sewer drainage system is structured as a tree. Water enters the system at n nodes numbered from 0 to n-1 and flows through the tree to the root, which has the number 0.

The tree structure is defined by an array parent, where parent[i] = j means that water flows from node i to its direct parent node j. Water exits the system after it flows through the root, so the root has no parent, represented as parent[0] = -1. The value in input[i] denotes the amount of water that enters the sewer system at node i. This excludes water that flows into i from its children.

The total flow through a node is thus the flow that enters at that node, plus the sum of the total flows of all of its children.

Your task is to divide the system into two smaller pieces by cutting one branch so that the total flows of the resulting subtrees are as close as possible.

Example:

parent = [-1, 0, 0, 1, 1, 2] 
input = [1, 2, 2, 1, 1, 1]
Input
Cut the branch between nodes 1 and 0. 

The partition {0, 2, 5) has total flow input[0] + input[2] + input[5] = 1+2+1 = 4. 
The partition {1, 3, 4) has total flow input[1] + input[3] + input[4] = 2 + 1 + 1 = 4. 

The absolute difference between the total flows of the two new sewer systems is 4 -4 = 0. It's not possible for a different division to achieve a smaller difference than 0, so the final answer is 0. 