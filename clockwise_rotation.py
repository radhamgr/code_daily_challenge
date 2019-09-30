
def clockwise_rotation90(A):
    N=len(A[0])
    for i in range(N//2):
        for j in range(i,N-i-1):
            temp = A[i][j]
            A[i][j] = A[N-1-j][i]
            A[N-1-j][i] = A[N-1-i][N-1-j]
            A[N-1-i][N-1-j] = A[j][N-1-i]
            A[j][N-1-i] = temp
def printing(A):
    N=len(A[0])
    for i in range(N):
        print(A[i])
A = [[1, 2, 3, 4], 
     [5, 6, 7, 8],  
     [9, 10, 11, 12],  
     [13, 14, 15, 16]]
clockwise_rotation90(A)
printing(A) 
# Test case 2 
mat = [ [1, 2, 3 ], 
        [4, 5, 6 ], 
        [7, 8, 9 ] ] 
clockwise_rotation90(mat)
printing(mat)
  
# Test case 3 
mat1 = [ [1, 2 ], 
        [4, 5 ] ] 
clockwise_rotation90(mat1)
printing(mat1)