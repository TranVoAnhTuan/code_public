import numpy as np 


def solve(A):
    row, col = A.shape
    for i in range(row):
        if A[i,i] == 0:
            for j in range(i+1, row):
                if A[i,j] != 0:
                    A[[i,j]] = A[[j,i]]
        A[i] = A[i]/A[i,i]
        for j in range(i+1, row):
            A[j] = A[j] - A[j,i] * A[i]
    ans = np.zeros(row)
    for i in range(row-1, -1, -1):
        ans[i] = A[i,-1]
        for j in range(i+1, row):
            ans[i] -= A[i,j]*ans[j]
    return ans;

A = np.array([[8,-3,2,20],[4,11,-1,33],[6,3,12,36]], dtype= float)
print(solve(A))
