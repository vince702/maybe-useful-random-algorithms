

def main():
 x = [1,3,2,5,8]; y = [2,6,4,7]
 print interlacingSubsequence(x,y)
    
def interlacingSubsequence(x,y):
    

    
 x = x; y = y;
 m = len(x); n = len(y);
 sorts = sorted(x)
 print sorts
 set(sorts)
 sorts.append(max(max(y)+1,max(x)+1))
 
 size = np.zeros((len(y),len(x),max(sorts)+1))
 sol = np.zeros((len(y),len(x),max(sorts)+1),dtype = list)
 for i in range(0,n):
     for j in range(0,m):
         for k in sorts:
             sol[i,j,k] = [];
             
             
 for i in range(0,n):
     for j in range(0,m):
         for k in sorts:
            
             if x[j] < y[i] and y[i] < k:
               size[i,j,k] = max(2 + size[i-1,j-1,x[j]], size[i,j-1,k], size[i-1,j,k])
               if size[i,j,k] == 2 + size[i-1,j-1,x[j]]:
               
                 for a in sol[i-1,j-1,x[j]]:
                   sol[i,j,k].append(a) 
                 sol[i,j,k].append(x[j]); sol[i,j,k].append(y[i])
               elif size[i,j,k] == size[i-1,j,k]:
                 for a in sol[i-1,j,k]:
                     
                   sol[i,j,k].append(a) 
               else:
                 for a in sol[i,j-1,k]:
                     sol[i,j,k].append(a)   
                 
               
             else:
                 size[i,j,k] = max( size[i,j-1,k], size[i-1,j,k])
                 if size[i,j,k] == size[i-1,j,k]:
                    for a in  sol[i-1,j,k]:
                      sol[i,j,k].append(a)
                      
                 else:
                    for a in sol[i,j-1,k]:
                     sol[i,j,k].append(a) 
                
            # print size[i,j,k],i,j


 return sol[n-1,m-1,max(y)+1]

main()



