from collections import deque

def sol(arr, k):
	N = len(arr)
	nge_arr = [ N ] * N
	st = deque()
	for i in range(0, N):
		while len(st) and arr[i] > arr[st[-1]]:
			top_ind = st.pop()
			nge_arr[top_ind] = i
		st.append(i)
	i, j = 0, 0
	ans = [0] * (N - k + 1)
	while i <= N - k:

		limit = i + k - 1
		if j < i or j>limit:
			j = i
		# find max in k elements

		prev_j = j
		while j<N and j <= limit:
			print("st", "j", j, nge_arr[j], "prev_j",prev_j)
			prev_j = j
			j = nge_arr[j]
			print("end", j, prev_j)
		print(prev_j)
		ans[i] = arr[prev_j]
		i+=1
	return ans



if __name__ == '__main__':
	arr =  [2, 9, 3, 8, 1, 7, 12, 6, 14, 4, 32, 0, 7, 19, 8, 12, 6]
	k = 4
	print(sol(arr, k))