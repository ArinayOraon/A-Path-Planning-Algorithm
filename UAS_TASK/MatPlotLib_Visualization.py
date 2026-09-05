import matplotlib.pyplot as plt
from A_Star_Algo import a_star

def plot_maker(grid,start_node,goal_node):
    value = a_star(grid,start_node,goal_node)
    path = value[0]

    x1_values = []
    y1_values = []
    x2_values = []
    y2_values = []

    for i in path:
        x1_values.append(i[0])
        y1_values.append(i[1])

    nodes_explored = value[3]

    for key in nodes_explored:
        x2_values.append(key[0])
        y2_values.append(key[1])

    plt.plot(x1_values,y1_values,color = "red")
    plt.scatter(x2_values,y2_values)
    plt.show()




