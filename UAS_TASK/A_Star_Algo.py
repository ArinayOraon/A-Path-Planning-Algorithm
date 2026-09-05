import math
import heapq

def get_heuristics(a,b):
    # Distance from current node to goal
    return math.sqrt(((a[0]-b[0])*(a[0]-b[0])) + ((a[1]-b[1])*(a[1]-b[1])))

def get_childern(node, given_grid):
    #Total no of rows and coloumns
    rows = len(given_grid)
    cols = len(given_grid[0])

    #Coordinate of current node
    curr_row, curr_col = node

    #Possible directions (up,down,right,left)
    directions = [
        (-1,0),
        (1,0),
        (0,1),
        (0,-1)
    ]

    children = []

    #Possible coordinates of the next node
    for diff_row, diff_col in directions:
        next_row = curr_row + diff_row
        next_col = curr_col + diff_col

        #Checking if the node is in the grid
        if 0<= next_row < rows and 0 <= next_col < cols:
            #Checking if the node is an obstacle
            if given_grid[next_row][next_col] == ".":
                children.append((next_row,next_col))

    return children

def a_star(given_grid, start_node, goal_node):

    #The priority queue
    priority_q = []

    #Dictionary of the parent node of every children node. This is also used to store all the explored nodes
    parent_nodes ={}

    #For A* : f(n) = f(cost) + f(heuristics)
    cost = {
        start_node:0
    }

    f_n_score = {
        start_node:get_heuristics(start_node,goal_node)
    }

    heapq.heappush(priority_q,(f_n_score[start_node],start_node))

    while priority_q:

        priority, curr_node = heapq.heappop(priority_q)

        #Checking if the current node has already been explored with a better priority
        if priority != f_n_score.get(curr_node,float("inf")):
            continue

        if curr_node == goal_node:
            best_path = []

            while curr_node in parent_nodes:
                best_path.append(curr_node)
                curr_node = parent_nodes[curr_node]
            best_path.append(start_node)
            best_path.reverse()
            total_cost = 0
            for i in best_path:
                total_cost =total_cost + cost[i]
            return [best_path,len(parent_nodes),total_cost,parent_nodes]

        for children in get_childern(curr_node,given_grid):

           will_cost = cost[curr_node] + 1 

           if will_cost < cost.get(children, float("inf")):

               parent_nodes[children] = curr_node

               cost[children] = will_cost

               f_n_score[children] = (will_cost + get_heuristics(children,goal_node))

               heapq.heappush(priority_q,(f_n_score[children],children))

    return None,parent_nodes





