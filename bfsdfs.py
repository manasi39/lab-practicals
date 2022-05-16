graph={'4':['6','2'],'6':['5','3'],'2':[],'5':[],'3':['1'],'1':[]}

#BFS
visit=[]
q=[]

def bfs(visit,graph,node):
	visit.append(node)
	q.append(node)

	while q:
		m=q.pop(0)
		print(m, end=" ")
		for n in graph[m]:
			if n not in visit:
				visit.append(n)
				q.append(n)

print("BFS")
bfs(visit,graph,'4')




#DFS
graph={'4':['6','2'],'6':['5','3'],'2':[],'5':[],'3':['1'],'1':[]}

visit=set()

def dfs(visit,graph,node):
	if node not in visit:
		print(node,end=" ")
		visit.add(node)
		for n in graph[node]:
			dfs(visited,graph,n)

print("DFS")
dfs(visit,graph,'4')
