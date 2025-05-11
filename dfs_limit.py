#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
vanilla breadth first search 
- relies on  Puzzle8.py module

@author: milos
"""

from Puzzle8 import *


 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### depth limited dfs ler96

def depth_first_search_limit(problem, limit):
    expanded = [0]
    generated = [0]
    max_depth = [0]

    def dfs_recursive(node, visited, limit):
        if node.g > limit:
            return None
        
        expanded[0] += 1
        max_depth[0] = max(max_depth[0], node.g)
        if node.goalp():
            return node

        visited.add_hash(node.state, node.g)
        optimal = None
        for new_state, cost in problem.generate_all_neighbor_states(node.state):
            child = TreeNode(problem, new_state, node, node.g + cost)
            if not visited.in_hashp(new_state) or child.g < visited.get_hash_value(new_state):
                visited.add_hash(new_state, child.g)
                generated[0] += 1
                result = dfs_recursive(child, visited, limit)
                if result:
                    if optimal is None or result.g < optimal.g:
                        optimal = result
        return optimal
    
    root = TreeNode(problem, problem.initial_state)
    visited = HashTable()
    visited.add_hash(root.state, root.g)

    optimal = dfs_recursive(root, visited, limit)
    if optimal:
        sol_path = optimal.path()
        num_moves = len(sol_path) - 1
        print("\nStats:")
        print("\nTotal nodes expanded: ", expanded[0])
        print("\nTotal nodes generated: ", generated[0])
        print("\nMaximum length of queue structure: ", max_depth[0])
        print("\nSolution path length: ", num_moves, "\n")
        return sol_path
    print("No solution")
    return NULL


limit = 20
problem=Puzzle8_Problem(Example1) 
output=  depth_first_search_limit(problem, limit)
print('Solution Example 1:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2) 
output=  depth_first_search_limit(problem, limit)
print('Solution Example 2:')
print_path(output)


wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example3) 
output=  depth_first_search_limit(problem, limit)
print('Solution Example 3:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example4) 
output=  depth_first_search_limit(problem, limit)
print('Solution Example 4:')
print_path(output)

# Solution to Example 5 may take too long to calculate using vanilla bfs
problem=Puzzle8_Problem(Example5) 
output=  depth_first_search_limit(problem, limit)
print('Solution Example 5:')
print_path(output)
 