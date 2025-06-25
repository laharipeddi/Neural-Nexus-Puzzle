import numpy as np

class node:
    def __init__(self,puzzle,parent,choosen_direction,cost,depth):
        self.puzzle=puzzle
        self.parent=parent
        self.choosen_direction=choosen_direction
        self.cost=cost
        self.depth=depth

class node_greedy:
    def __init__(self,puzzle,parent,choosen_direction,cost,depth,heuristic,h1):
        self.puzzle=puzzle
        self.parent=parent
        self.choosen_direction=choosen_direction
        self.cost=cost
        self.depth=depth
        self.heuristic=heuristic
        self.h1=h1



def manhatten_heuristic(puzzle):
    board=[]
    for i in range(3):
        for j in range(3):
            board.append(puzzle[i][j])
    return sum((abs((val-1)%3 - i%3) + abs((val-1)//3 - i//3))*val
        for i, val in enumerate(board) if val)

def to_string(puzzle,f):
    string="["
    if f==0:
        for i in range(3):
            string+="["+str(puzzle[i][0])+","+str(puzzle[i][1])+","+str(puzzle[i][2])+"]"
        return string+"]"
    else:
        return "[["+puzzle[0]+","+puzzle[1]+","+puzzle[2]+"]["+puzzle[3]+","+puzzle[4]+","+puzzle[5]+"],["+puzzle[6]+","+puzzle[7]+","+puzzle[8]+"]]"

        



def successor_function(prasent_state,f):
    a=prasent_state.puzzle
    successors=[]
    for i in range(3):
        for j in range(3):
            if(a[i][j]==0):
                if i>0:
                    prasent_board_state=np.copy(a)
                    prasent_board_state[i][j]=prasent_board_state[i-1][j]
                    prasent_board_state[i-1][j]=0
                    if f==1:
                        successors.append(node(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Down",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1))
                    elif f==2:
                        successors.append(node_greedy(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Down",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1,manhatten_heuristic(prasent_board_state),manhatten_heuristic(prasent_board_state)+prasent_state.cost+prasent_board_state[i][j]))
                    else:
                        successors.append(node(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Down",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1))
                    
                if i<2:
                    prasent_board_state=np.copy(a)
                    prasent_board_state[i][j]=prasent_board_state[i+1][j]
                    prasent_board_state[i+1][j]=0
                    if f==1:
                        successors.append(node(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Up",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1))
                    elif f==2:
                        successors.append(node_greedy(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Up",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1,manhatten_heuristic(prasent_board_state),manhatten_heuristic(prasent_board_state)+prasent_state.cost+prasent_board_state[i][j]))
                    else:
                        successors.append(node(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Up",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1))
                    
                if j>0:
                    prasent_board_state=np.copy(a)
                    prasent_board_state[i][j]=prasent_board_state[i][j-1]
                    prasent_board_state[i][j-1]=0
                    if f==1:
                        successors.append(node(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Right",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1))
                    elif f==2:
                        successors.append(node_greedy(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Right",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1,manhatten_heuristic(prasent_board_state),manhatten_heuristic(prasent_board_state)+prasent_state.cost+prasent_board_state[i][j]))
                    else:
                        successors.append(node(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Right",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1))
                    
                if j<2:
                    prasent_board_state=np.copy(a)
                    prasent_board_state[i][j]=prasent_board_state[i][j+1]
                    prasent_board_state[i][j+1]=0
                    if f==1:
                        successors.append(node(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Left",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1))
                    elif f==2:
                        successors.append(node_greedy(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Left",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1,manhatten_heuristic(prasent_board_state),manhatten_heuristic(prasent_board_state)+prasent_state.cost+prasent_board_state[i][j]))
                    else:
                        successors.append(node(prasent_board_state,prasent_state,"Move "+str(prasent_board_state[i][j])+" Left",prasent_state.cost+prasent_board_state[i][j],prasent_state.depth+1))
                    
                return successors


def Integer_to_string(puzzle):
    string=""
    for a in range(3):
        for b in range(3):
            string=string+str(puzzle[a][b])
    return string
def check_goal(current,goal):
    for i in range(3):
        for j in range(3):
            if current[i][j]!=goal[i][j]:
                
                return False
    return True
def dfs(Start_puzzle,Goal_state  ):
    Starting_state=node(Start_puzzle,None,None,0,0)
    number_of_nodes_generated=1
    number_of_nodes_expanded=0
    number_of_nodes_popped=0
    max_fringe_size=0
    closedSet=set()
    Fringe=[]
    Fringe.append(Starting_state)
    while Fringe:
        if max_fringe_size< len(Fringe):
            max_fringe_size=len(Fringe)
        current_puzzle=Fringe.pop()
        number_of_nodes_popped+=1
        if(check_goal(current_puzzle.puzzle,Goal_state)):
            print("NODES EXPANDED:",number_of_nodes_expanded)
            print("NODES GENERATED:",number_of_nodes_generated)
            print("SOLUTION FOUND AT DEPTH ",current_puzzle.depth," WITH COST ",current_puzzle.cost,"\n")
            path=[]
            while current_puzzle.parent is not None:
                path.append(current_puzzle.choosen_direction)
                current_puzzle=current_puzzle.parent
            path.reverse()
            print(*path, sep = "\n")
            return ""
        if Integer_to_string(current_puzzle.puzzle) in closedSet:
            continue
        else:
            closedSet.add(Integer_to_string(current_puzzle.puzzle))
            number_of_nodes_expanded+=1
            successors=successor_function(current_puzzle,0)
            for successor in successors:
                number_of_nodes_generated+=1
                Fringe.append(successor)

    return -1






def greedy(Start_puzzle,Goal_state  ):
    Starting_state=node_greedy(Start_puzzle,None,None,0,0,0,0)
    number_of_nodes_generated=1
    number_of_nodes_expanded=0
    number_of_nodes_popped=0
    max_fringe_size=0
    closedSet=set()
    Fringe=[]
    Fringe.append(Starting_state)
    while Fringe:
        if max_fringe_size< len(Fringe):
            max_fringe_size=len(Fringe)
        Fringe.sort(key = lambda c: c.heuristic)
        current_puzzle=Fringe.pop(0) 
        number_of_nodes_popped+=1
        if(check_goal(current_puzzle.puzzle,Goal_state)):
            print("NODES EXPANDED:",number_of_nodes_expanded)
            print("NODES GENERATED:",number_of_nodes_generated)
            print("SOLUTION FOUND AT DEPTH ",current_puzzle.depth," WITH COST ",current_puzzle.cost,"\n")
            path=[]
            while current_puzzle.parent is not None:
                path.append(current_puzzle.choosen_direction)
                current_puzzle=current_puzzle.parent
            path.reverse()
            print(*path, sep = "\n")
            return ""
        if Integer_to_string(current_puzzle.puzzle) in closedSet:
            continue
        else:
            closedSet.add(Integer_to_string(current_puzzle.puzzle))
            number_of_nodes_expanded+=1
            successors=successor_function(current_puzzle,2)
            for successor in successors:
                number_of_nodes_generated+=1
                Fringe.append(successor)

    return -1





def a_star(Start_puzzle,Goal_state  ):
    Starting_state=node_greedy(Start_puzzle,None,None,0,0,0,0)
    number_of_nodes_generated=1
    number_of_nodes_expanded=0
    number_of_nodes_popped=0
    max_fringe_size=0
    closedSet=set()
    Fringe=[]
    Fringe.append(Starting_state)
    while Fringe:
        if max_fringe_size< len(Fringe):
            max_fringe_size=len(Fringe)
        Fringe.sort(key = lambda c: c.h1)
        
        current_puzzle=Fringe.pop(0)
        number_of_nodes_popped+=1
        if(check_goal(current_puzzle.puzzle,Goal_state)):
            print("NODES EXPANDED:",number_of_nodes_expanded)
            print("NODES GENERATED:",number_of_nodes_generated)
            print("SOLUTION FOUND AT DEPTH ",current_puzzle.depth," WITH COST ",current_puzzle.cost,"\n")
            path=[]
            while current_puzzle.parent is not None:
                path.append(current_puzzle.choosen_direction)
                current_puzzle=current_puzzle.parent
            path.reverse()
            print(*path, sep = "\n")
            return ""
        if Integer_to_string(current_puzzle.puzzle) in closedSet:
            continue
        else:
            closedSet.add(Integer_to_string(current_puzzle.puzzle))
            number_of_nodes_expanded+=1
            successors=successor_function(current_puzzle,2)
            for successor in successors:
                number_of_nodes_generated+=1
                Fringe.append(successor)

    return -1





def ids(start,goal  ):
    depth=0
    while(True):
        solution=ids_recursion(start,goal,depth  )
        depth+=1
        if solution!=None:
            return ""
    return False

def ids_recursion(Start_puzzle,Goal_state,depth  ):
        Starting_state=node(Start_puzzle,None,None,0,0)
        number_of_nodes_generated=1
        number_of_nodes_expanded=0
        number_of_nodes_popped=0
        max_fringe_size=0
        closedSet=set()
        Fringe=[]
        Fringe.append(Starting_state)
        while Fringe:
            if max_fringe_size< len(Fringe):
                max_fringe_size=len(Fringe)
            current_puzzle=Fringe.pop()
            number_of_nodes_popped+=1
            if(check_goal(current_puzzle.puzzle,Goal_state)):
                print("NODES EXPANDED:",number_of_nodes_expanded)
                print("NODES GENERATED:",number_of_nodes_generated)
                print("SOLUTION FOUND AT DEPTH ",current_puzzle.depth," WITH COST ",current_puzzle.cost,"\n")
                path=[]
                while current_puzzle.parent is not None:
                    path.append(current_puzzle.choosen_direction)
                    current_puzzle=current_puzzle.parent
                path.reverse()
                print(*path, sep = "\n")
                return 1
            if Integer_to_string(current_puzzle.puzzle) in closedSet:
                continue
            if current_puzzle.depth==depth:
                continue
            else:
                closedSet.add(Integer_to_string(current_puzzle.puzzle))
                number_of_nodes_expanded+=1
                successors=successor_function(current_puzzle,0)
                for successor in successors:
                    number_of_nodes_generated+=1
                    Fringe.append(successor)

        return None

def dls(Start_puzzle,Goal_state,depth  ):
        Starting_state=node(Start_puzzle,None,None,0,0)
        number_of_nodes_generated=1
        number_of_nodes_expanded=0
        number_of_nodes_popped=0
        max_fringe_size=0
        closedSet=set()
        Fringe=[]
        Fringe.append(Starting_state)
        while Fringe:
            if max_fringe_size< len(Fringe):
                max_fringe_size=len(Fringe)
            current_puzzle=Fringe.pop()
            number_of_nodes_popped+=1
            if(check_goal(current_puzzle.puzzle,Goal_state)):
                print("NODES EXPANDED:",number_of_nodes_expanded)
                print("NODES GENERATED:",number_of_nodes_generated)
                print("SOLUTION FOUND AT DEPTH ",current_puzzle.depth," WITH COST ",current_puzzle.cost,"\n")
                path=[]
                while current_puzzle.parent is not None:
                    path.append(current_puzzle.choosen_direction)
                    current_puzzle=current_puzzle.parent
                path.reverse()
                print(*path, sep = "\n")
                return ""
            if current_puzzle.depth==depth:
                continue
            else:
                successors=successor_function(current_puzzle,1)
                for successor in successors:
                    number_of_nodes_generated+=1
                    Fringe.append(successor)

        return -1


def ucs(Start_puzzle,Goal_state  ):
    Starting_state=node(Start_puzzle,None,None,0,0)
    number_of_nodes_generated=1
    number_of_nodes_expanded=0
    number_of_nodes_popped=0
    max_fringe_size=0
    closedSet=set()
    Fringe=[]
    Fringe.append(Starting_state)
    while Fringe:
        if max_fringe_size< len(Fringe):
            max_fringe_size=len(Fringe)
        Fringe.sort(key = lambda c: c.cost)
        current_puzzle=Fringe.pop(0)
        number_of_nodes_popped+=1
        if(check_goal(current_puzzle.puzzle,Goal_state)):
            print("NODES EXPANDED:",number_of_nodes_expanded)
            print("NODES GENERATED:",number_of_nodes_generated)
            print("SOLUTION FOUND AT DEPTH ",current_puzzle.depth," WITH COST ",current_puzzle.cost,"\n")
            path=[]
            while current_puzzle.parent is not None:
                path.append(current_puzzle.choosen_direction)
                current_puzzle=current_puzzle.parent
            path.reverse()
            print(*path, sep = "\n")
            return ""
        if Integer_to_string(current_puzzle.puzzle) in closedSet:
            continue
        else:
            closedSet.add(Integer_to_string(current_puzzle.puzzle))
            number_of_nodes_expanded+=1
            successors=successor_function(current_puzzle,0)
            for successor in successors:
                number_of_nodes_generated+=1
                Fringe.append(successor)

    return -1




def bfs(Start_puzzle,Goal_state  ):
    Starting_state=node(Start_puzzle,None,None,0,0)
    number_of_nodes_generated=1
    number_of_nodes_expanded=0
    number_of_nodes_popped=0
    max_fringe_size=0
    closedSet=set()
    Fringe=[]
    Fringe.append(Starting_state)
    while Fringe:
        if max_fringe_size< len(Fringe):
            max_fringe_size=len(Fringe)
        current_puzzle=Fringe.pop(0)
        number_of_nodes_popped+=1
        if(check_goal(current_puzzle.puzzle,Goal_state)):
            print("NODES EXPANDED:",number_of_nodes_expanded)
            print("NODES GENERATED:",number_of_nodes_generated)
            print("SOLUTION FOUND AT DEPTH ",current_puzzle.depth," WITH COST ",current_puzzle.cost,"\n")
            path=[]
            while current_puzzle.parent is not None:
                path.append(current_puzzle.choosen_direction)
                current_puzzle=current_puzzle.parent
            path.reverse()
            print(*path, sep = "\n")
            return ""
        if Integer_to_string(current_puzzle.puzzle) in closedSet:
            continue
        else:
            
            closedSet.add(Integer_to_string(current_puzzle.puzzle))
            number_of_nodes_expanded+=1
            successors=successor_function(current_puzzle,0)
            for successor in successors:
                number_of_nodes_generated+=1
                Fringe.append(successor)
    return -1



START = []
print("Enter the Start state:-\n")
for _ in range(3):
    row = list(map(int, input().split()))
    START.append(row)

GOAL = np.array([[1,2,3], [4,5,6], [7,8,0]])
method=input("Enter the name of the Algorithm:-")


if method== "ids":
    solution=ids(START,GOAL)
    print(solution)
elif method=="dfs":
    solution=dfs(START,GOAL )
elif method=="bfs":
    solution=bfs(START,GOAL )
    print(solution)
elif method=="ucs":
    solution=ucs(START,GOAL )
    print(solution)
elif method=="dls":
    depth=int(input("enter the limit:-"))
    solution=dls(START,GOAL,depth )
    print(solution)
elif method=="greedy":
    solution=(greedy(START,GOAL ))
    print(solution)
elif method=="a*":
    solution=(a_star(START,GOAL ))
    print(solution)
    
