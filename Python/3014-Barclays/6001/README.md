<br/>Arya is attempting to solve a math problem. In this proble, she is given a tree with N nodes, indexed from 1 to N where the root node is indexed as 1. Each node of the tree has a defined value. She wants to trace a path from one leaf to another leaf in such a way that will award her the maximum score for that path. The score of a path is defined as the product of node values along the path.
<p> Input:</br>
The first line of the input consists of an integer - num, representing the number of nodes in the tree (N).
The second line consists N space separated integers representing the value of each node in the tree. </p>
<p>The third line consists of two space-separate integers - numEdges and numNodes, representing the number of edges(E) and the number of nodes forming an edge (where V = 2 always), respectively.</p>
<p>The next E lines consist of two space-separated integers - start and end, representing the indices of the starting node and ending node of an edge of the tree.
</p>
<p>Output:
<br/>
Print an integer representing the maximum possible score
</p>
<br/>Write an algorithm to find the maximum possible score.

<br/>Example:
<br/>Input:
<br/>4
<br/>-1 2 3 2
<br/>3 2
<br/>1 2
<br/>1 3
<br/>3 4
<br/>Output:
<br/>-12

<br/>Explanation
<span>
 1(-1)
 /    \
2(2)   3(3)
     /
   4(2)
</span>