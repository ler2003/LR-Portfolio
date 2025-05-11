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
 #### breadth first search no cyclic state repeats ler96         
        
def check_cyclic_repeats(node):
    curr_state = node.state
    prev = node.parent
    while prev:
        if prev.state == curr_state:
            return True
        prev = prev.parent
    return False

def breadth_first_search_cycles(problem):
    queue =deque([])
    root=TreeNode(problem,problem.initial_state)
    queue.append(root)
    expanded = 0
    generated = 0
    max_queue = 0  
    while len(queue)>0:
        max_queue = max(max_queue, len(queue))
        next=queue.popleft()
        expanded +=1
        if next.goalp():
            sol_path = next.path()
            num_moves = len(sol_path) -1
            print("\nStats:")
            print("\nTotal nodes expanded: ", expanded)
            print("\nTotal nodes generated: ", generated)
            print("\nMaximum length of queue structure: ", max_queue)
            print("\nSolution path length: ", num_moves, "\n")

            del(queue)
            return sol_path
            
        new_nodes=next.generate_new_tree_nodes()
        for new_node in new_nodes:
            if not check_cyclic_repeats(new_node):
                queue.append(new_node)
                generated+=1     
    print('No solution')
    return NULL

  
problem=Puzzle8_Problem(Example1) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 1:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 2:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example3) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 3:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example4) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 4:')
print_path(output)

# Solution to Example 5 may take too long to calculate using vanilla bfs
problem=Puzzle8_Problem(Example5) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 5:')
print_path(output)
 