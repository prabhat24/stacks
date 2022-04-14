from sys import stdin
from collections import deque


#write your code here
def sol(arr):
    N = len(arr)
    
    # setr
    st = deque()
    ansr = [len(arr)] * len(arr) 
    for i in range(0, N):
        while len(st) and arr[i] < arr[st[-1]]:
            top_ind = st.pop()
            ansr[top_ind] = i
        st.append(i)

    # setl
    st = deque()
    ansl = [-1] * len(arr)
    for i in range(N-1, -1, -1):
        while len(st) and arr[i] < arr[st[-1]]:
            top_ind = st.pop()
            ansl[top_ind] = i
        st.append(i)
    
    maxa = - ((1<<31) -1)
    for i in range(len(ansl)):
        maxa = max(maxa, arr[i]*(ansr[i] - ansl[i] -1))
    return maxa