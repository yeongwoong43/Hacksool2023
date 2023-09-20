from metro_line import Station
from metro_line import SungDongMetroLines

def bfs(graph, start, end, level):
	queue = []
	queue.append(start)
	print(queue)
	visited = [False] * 15
	visited[start] = True
	while queue:
		s = len(queue)
		for i in range(s):
			cur = queue[0]
			queue.pop(0)
			for j in graph[cur]:
				if j == end:
					print(level)
					return
				if visited[j] == False:
					queue.append(j)
					visited[j] = True
		level += 1
graph = []
SungDongMetroLines(graph)
level = 1
bfs(graph, 1, 3, level)