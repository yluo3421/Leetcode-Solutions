class Solution:
    def find_max_path_product(num_nodes, node_values, numEdges, numNodes, start_end_arr):
        # thoughts:
        # this question is similar to max path sum
        # but the input is not tree node thus not able to 
        # implement the same methodology.
        # With the start and end edges specified, it is possible
        # to identify leaf nodes directly.
        # we could find out all leaf nodes and use dfs to see all results
        # loop through all leaf nodes and record all answers
        # return the maximum.
        