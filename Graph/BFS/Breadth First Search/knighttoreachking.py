
class cell:
    def __init__(self,x,y,dist) -> None:
        self.x=x
        self.y=y
        self.dist=dist
def isInsinde(x,y,size):

    if (x>=1 and x<=size) and (y>=1 and y<=size):
        return True
    else:
        return False
    
def minimum_step_reach_king(knight_pos:tuple,target_pos:tuple,board_size:int):
    #Setting up positions for a knight to move 
    move_x=[2,2,-2,-2,1,1,-1,-1]
    move_y=[1,-1,1,-1,2,-2,-2,2]
    #Now just breadth first search
    q=[]
    #create 2d board named visited
    visited=[[False for i in range(board_size+1)] for j in range(board_size+1)]
    #create a 2d board for defining path
    path_s=[[(False,False) for i in range(board_size+1)] for j in range(board_size+1)]
    #append knight position to queue
    knight_cell=cell(knight_pos[0],knight_pos[1],0)
    q.append(knight_cell)
    visited[knight_cell.x][knight_cell.y]=True
    path_s[knight_cell.x][knight_cell.y]=(knight_cell.x,knight_cell.y)
    #Now we will check every cell and from where to reach king's position
    while len(q)!=0:
        temp_cell=q.pop(0)
        if temp_cell.x==target_pos[0] and temp_cell.y==target_pos[1]:
            print(f"Reachable king after {temp_cell.dist} steps")
            #print("Printing the whole path")
            #print(path_s)
            return temp_cell.dist,path_s
        else:
            #we will check every position from where you can move to
            for i in range(8):
                x=temp_cell.x+move_x[i]
                y=temp_cell.y+move_y[i]

                if isInsinde(x,y,board_size) and visited[x][y]==False:
                    visited[x][y]=True
                    path_s[x][y]=(temp_cell.x,temp_cell.y)
                    q.append(cell(x,y,temp_cell.dist+1))

    print("Cannot reach the king")
    return False

if __name__=='__main__':
    N=30
    knight_pos=(1,1)
    target_pos=(30,30)
    res,path=minimum_step_reach_king(knight_pos,target_pos,N)
    print(res)
    print()
    position=target_pos
    while position!=knight_pos:
        position=path[position[0]][position[1]]
        print(position,end="<--")

    

    
