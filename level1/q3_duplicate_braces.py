import sys
from collections import deque

def is_duplicate(string):
    st = deque()
    for ch in string :
        if ch == ")":
            if st[-1] == "(":
                return False
            else:
                while len(st) and st[-1] != "(":
                    st.pop()
                    st.pop()
        else:
            st.append(ch)
    return True



if __name__ == '__main__':
    print("abc")
    string = input()
    print(str(is_duplicate(string)).lower())