class CustomStack:
       
    def __init__(self , cap):
        self.cap = cap
        self.tos = -1
        self.arr = []
        self.arr = [0] * cap
       
    def size(self):
        return self.tos + 1
       

    def push(self , data):
        if self.size() >= self.cap:
            print("Stack overflow")
        else:
            self.tos += 1
            self.arr[self.tos] = data
   
       
    def top(self):
        if self.tos>=0:
            return self.arr[self.tos]
        else:
            print("Stack underflow")
            return -1
       
       
   
    def pop(self):
        if self.tos>=0:
            top = self.top()
            self.tos -= 1
            return top
        else:
            print("Stack underflow")
       
       
    def display(self):
        res = ""    
        for i in range(self.tos, -1, -1):
            res = res + str(self.arr[i]) + " "
        print(res)
        
       


def main():
   
    n = int(input());
   
    inpStr = str(input()).split(" ")
    st = CustomStack(n)
   
    while inpStr[0] != "quit":
        if inpStr[0].strip() == "push":
            val = inpStr[1]
            st.push(val)
        elif inpStr[0].strip() == "pop":
            val = st.pop()
            if val != -1:
                print(val)
        elif inpStr[0].strip() == "top":
            val = st.top()
            if val != -1:
                print(val)
        elif inpStr[0].strip() == "size":
            print(st.size())
        elif inpStr[0].strip() == "display":
            st.display()
           
        inpStr = str(input()).split(" ")
           
   
main()