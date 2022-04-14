from collections import deque

def sol(arr, N):
    st = deque()
    new_arr = [0] * N
    for i in range(0, N):
        if len(st) and arr[i] > arr[st[-1]]:
            while len(st) and arr[i] > arr[st[-1]]:
                top_ind = st.pop()
                new_arr[top_ind] = arr[i]
                print("new_arr", new_arr, "st", st)
        st.append(i)

    while len(st):
        top_ind = st.pop()
        new_arr[top_ind] = -1
    return new_arr


if __name__ == '__main__':
    arr = [2, 5, 9, 3, 1, 12, 6, 8, 7]
    print(sol(arr, len(arr)))
