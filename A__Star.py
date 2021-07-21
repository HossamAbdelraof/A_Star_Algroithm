import numpy as np
import matplotlib.pyplot as plt

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self,position=(0,0), parent=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    



                  
      
def A_Star(start, end, maze):
    
    ## define Start and End nodes
    Start_N = Node(start)
    End_N = Node(end)
    
    ## set open and Closed List
    open_list = [Start_N]
    closed_list = []
    
    ## init childs posision // square around the node 
    ## unless there is a block
    Child_Pos = [(0, -1), ( 0, 1), (-1, 0), (1, 0),
                 (-1,-1), (-1, 1), (1, -1), (1, 1)]
      
    ## while openlist is not empity
    while open_list:
        ## our point is the last point in the open list
        This_Poink = open_list[-1]
        ind = -1
        
        ## checking if any point with lower coast in the open list
        ##@@ we chose the lowest coast point
        
        for inx, poink in enumerate(open_list):
            ##  enumerate return the value and it's index 
            
            if (This_Poink.f > poink.f):
            ## if the we found lower coast point will replace current point
            ## and current index
                This_Poink = open_list[inx]
                ind = inx
        
        ## add current point to closed list and drop it from open list
        closed_list.append( open_list.pop(ind) )
    
        
      
        ## if we reached the goal 
        ## add teh posision of this point and it's parent till starting point
        ### and return reversed path
        if This_Poink == End_N:
            path = []
            
            while This_Poink:
                
                path.append(This_Poink.position)
                This_Poink = This_Poink.parent
          
            return path[::-1] 
        
        
        ## if not reached 
        
        ## add childrens to the point and repeat 
        for pos in Child_Pos:
        ## loop in every child posision   
        
            ## add child posision to current posision
            New_Child = tuple(np.add(This_Poink.position, pos))
            
            ## check if we didnot pass the porders or in wall point
            try:
                if ((-1 in New_Child) or (maze[New_Child[0]][New_Child[1]] == 9)):
                    continue
            except IndexError:
                continue
            
            ## creat child node
            This_Child = Node(New_Child, This_Poink)
            
            if ((This_Child in open_list)) or (This_Child in closed_list):
                continue
            ## calculate child G,H,F
            
            ## the + child G coast 1, and X child coast 2
            if (0 in pos):
                This_Child.g = This_Child.parent.g +1
            else:
                This_Child.g = This_Child.parent.g +2
                
            ## calculate H for the child 
            This_Child.h = cal_distance(This_Child.position, end)
            
            ## calculate F for the child
            This_Child.f = This_Child.g + This_Child.h
            
            ## add child to open list
            open_list.append(This_Child)
        ## repeat the operation 
    print("no_solution")
    return
            
          


    
## fun to calculate distancd  between current point and end point
def cal_distance(point1, point2):
    x = point2[0] - point1[0]
    y = point2[1] - point1[1]
     
    return np.sqrt(x**2 + y**2)
      
## function to draw solution of the maze
def plot_sol(start, end, path, maze):
    
    for i in path:
        maze[i[0]][i[1]] = 5
        
    maze[start[0]][start[1]] = 7
    maze[end[0]][end[1]] = 8
    
    plt.imshow(maze)
 
      
      
      
      
def main():
     
    maze1 = np.array([[2, 9, 1, 1, 1, 1, 9, 9, 3, 1 ],
                      [1, 9, 1, 9, 1, 1, 1, 9, 1, 1 ],
                      [1, 1, 1, 9, 1, 1, 9, 9, 9, 1 ],
                      [9, 9, 9, 9, 1, 9, 9, 9, 1, 1 ],
                      [1, 1, 1, 9, 1, 1, 1, 1, 1, 9 ],
                      [1, 9, 1, 1, 1, 1, 9, 1, 9, 9 ],
                      [1, 9, 9, 9, 9, 9, 9, 9, 9, 1 ],
                      [1, 1, 1, 9, 9, 9, 1, 1, 1, 1 ],
                      [1, 9, 1, 1, 1, 1, 1, 9, 9, 1 ]])
    
    maze2 =        [[1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 9, 1, 1, 1, 3, 1],
                    [1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    start = (0, 0)
    end1 = (0, 8)
    end2 = (7, 8)

    path = A_Star(start, end1, maze1)
    plot_sol(start, end1, path, maze1)
          
      
if __name__ == '__main__':
    main()
      
      
      
      
      