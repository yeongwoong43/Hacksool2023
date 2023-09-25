# from metro_line import Station
from metro_line import SungDongMetroLines


def bfs(graph_, start_, end_, level_):
	queue = [start_]
	visited = [False] * 15
	visited[start_] = True
	while queue:
		s = len(queue)
		for i in range(s):
			cur = queue[0]
			queue.pop(0)
			for j in graph_[cur]:
				if j == end_:
					print("You must pass through " + str(level_) + " station(s)")
					return
				if not visited[j]:
					queue.append(j)
					visited[j] = True
		level_ += 1


graph = []
SungDongMetroLines(graph)
level = 1
start = int(input("Enter the starting station as a number 0 - 14\n"))
end = int(input("Enter the ending station as a number 0 - 14\n"))
bfs(graph, start, end, level)
