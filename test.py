import copy 
def isPossible(storage, idx):
    dx,dy=[0,1,0,-1],[1,0,-1,0]
    
    for i in range(4):
        x=idx[0]+dx[i]
        y=idx[1]+dy[i]
        
        if x<0 or y<0:
            return True
        
        if x>=len(storage[0]) or y>=len(storage):
            return True
        
        if storage[y][x] == 'x':
            storage[y][x]='o'
            if canAcess(storage,[x,y]):
                storage[y][x]='x'
                return True
            storage[y][x]='x'
            
                 

    return False


def canAcess(storage,idx):
    dx,dy=[0,1,0,-1],[1,0,-1,0]
    
    if idx[0]==0 or idx[1]==0:
        return True
        
    if idx[0]>=len(storage[0]) or idx[1]>=len(storage):
        return True
    
    for i in range(4):
        x=idx[0]+dx[i]
        y=idx[1]+dy[i]
        
        if storage[y][x] == 'x':
            storage[y][x]='o'
            if canAcess(storage,[x,y]):
                storage[y][x]='x'
                return True
            storage[y][x]='x'
            
    return False
    


def solution(storage, requests):
    answer = 0
    fn_storage=[]
    for id in storage:
        fn_storage.append(list(id))
    storage=fn_storage
    
    
    for request in requests:
        
        
        fn_storage=copy.deepcopy(storage)
        if len(request)==1:
            
            for y in range(len(fn_storage)):
                for x in range(len(fn_storage[0])):
                    if fn_storage[y][x] ==request:            
                        if isPossible(fn_storage,[x,y]):
                            storage[y][x]='x'
            
            storage
            
        if len(request)==2:

            for y in range(len(storage)):
                for x in range(len(storage[0])):
                    # print(storage[y][x] == request[0])
                    if storage[y][x] ==request[0]:
                        storage[y][x]='x'
                
            
            
            
    for i in storage:
        for j in i:
            if j != 'x':
                answer+=1
    
    
    return answer




solution(["AZWQY", "CAABX", "BBDDA", "ACACA"],["A", "BB", "A"])

# ["AZWQY", "CAABX", "BBDDA", "ACACA"]	["A", "BB", "A"]	11
