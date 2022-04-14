from collections import deque


if __name__ == '__main__':
	stack = deque()

	# push operation
	stack.append(1)
	stack.append(2)
	print(stack)

	# pop operation
	print(stack.pop())

	# top operation
	print(stack[-1])
