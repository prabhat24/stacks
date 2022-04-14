class Stack:


	def __init__(self, max_cap):
		self.capacity = max_cap
		self.arr = [0] * self.capacity
		self.top = -1


	def size(self):
		return self.top+1


	def is_empty(self):
		return True if self.top == -1 else False

	# push operation
	def append(self, ele):
		if self.top + 1 > self.capacity:
			raise Exception("Stack Overflow")
		self.top +=1
		self.arr[self.top] = ele

	# pop operation
	def pop(self):
		if self.is_empty():
			raise Exception("Empty Stack, cannot pop")
		poped_ele = self.arr[-1]
		self.top -= 1
		return poped_ele

	# utility func to display stack
	def display(self):
		print(self.arr[0: self.top+1])

	def func_top(self):
		if self.is_empty():
			raise Exception("Empty Stack, cannot pop")
		return self.arr[self.top]



if __name__ == '__main__':
	
	# initialize stack
	st = Stack(10)

	# push operation
	st.append(1)
	st.append(2)
	st.display()

	# pop operation
	print(st.pop())
	st.display()

	# top operation
	print(st.func_top())

	# if empty operation
	print(st.is_empty())

