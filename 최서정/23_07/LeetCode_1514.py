class Solution:
	def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

		graph = defaultdict(list)

		for index in range(len(edges)):

			source , destination = edges[index]
			graph[source].append([destination, succProb[index]])
			graph[destination].append([source, succProb[index]])

		result = [0.0] * n

		result[start] = 1.0

		queue = deque([start])

		while queue:

			current_node = queue.popleft()

			for next_node , current_probability in graph[current_node]:

				if result[current_node] * current_probability > result[next_node]:

					result[next_node] = result[current_node] * current_probability

					queue.append(next_node)

		return result[end]
