from collections import deque
def bfs(name):
    neighbors_queue = deque()
    neighbors_queue += graph[name]
    searched = []
    while neighbors_queue:
        person = neighbors_queue.popleft()
        if not person in searched:
            if is_seller(person):
                print person + "is a mango seller"
                return True
            else:
                neighbors_queue += graph[person]
                searched.append(person)
    return False
def is_seller(name):
    return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print bfs("you")
