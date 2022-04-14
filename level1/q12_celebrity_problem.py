from collections import deque

def findCelebrity(arr, n):
    st = deque()
    for i in range(0,n):
        st.append(i)
    

    while len(st) >= 2:
        a = st.pop()
        b = st.pop()
        # check if a knows b
        if arr[a][b] == "1":
            st.append(b)
        elif arr[a][b] == "0":
            st.append(a)
    
    probable_celebrity = st[-1]
    for i in range(0, n):
        if arr[probable_celebrity][i] == "1":
            print("none")
            return
    for i in range(0, n):
        if i == probable_celebrity:
            continue
        else:
            if arr[i][probable_celebrity] == "0":
                print("none")
                return
    print(probable_celebrity)
    return
    