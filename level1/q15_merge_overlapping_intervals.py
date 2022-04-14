def take_first(ele):
	return ele[0]

class Solution(object):
    def merge(self, arr):
        N = len(arr)
        arr.sort(key=take_first)
        q = deque()
        q.append(arr[0])
        for i in range(1, N):
            last_schedule = q[-1]
            if arr[i][0] <= last_schedule[1]:
                # merge
                last_schedule[1] = max(arr[i][1], last_schedule[1])
            else:
                # push to stack
                q.append(arr[i])
        return list(q)