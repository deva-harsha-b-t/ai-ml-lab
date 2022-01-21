"""1. Implement A* Search algorithm"""


import sys

inf = 99999

g = [
     [0,4,3,inf,inf,inf,inf],
     [inf,0,inf,inf,12,5,inf],
     [inf,inf,0,7,10,inf,inf],
     [inf,inf,inf,0,2,inf,inf],
     [inf,inf,inf,inf,0,inf,5],
     [inf,inf,inf,inf,inf,0,16],
     [inf,inf,inf,inf,inf,inf,0]
    ]

h = [14,12,11,6,4,11,0]

src = 0
goal = 6

class astar:
    def __init__(self,cost,path):
        self.cost = cost
        self.path = path
     
     # A* Algorithm
    def astarfun(self,arr,new_item):
        while arr:
            cur_item = arr[0]
            cur_node = cur_item.path[-1]
            cur_cost = cur_item.cost
            cur_path = cur_item.path
            for i in range(len(h)):
                if g[cur_node][i]!=inf and g[cur_node][i]!=0:
                    new_cost = cur_cost - h[cur_node] + h[i] + g[cur_node][i]
                    new_path = cur_path.copy()
                    new_path.append(i)
                    if i==goal:
                        print(new_cost)
                        print(new_path)
                        return
                    new_item = astar(new_cost,new_path)
                    arr.append(new_item)
            arr.pop(0)
            arr = sorted(arr, key=lambda item: item.cost)

arr = []

new_item = astar(h[src],[src])
arr.append(new_item)
new_item.astarfun(arr,new_item)

