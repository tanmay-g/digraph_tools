import random

nodes = 25
edges = 150

length = 4
start_node = 0

remaining_edges = edges

name = 'test3.txt'

# -----------------------------------------------------------
steps = random.sample(xrange(nodes), length)
steps.sort()
steps.insert(0, start_node)
steps.append(start_node)

# -----------------------------------------------------------

f = open('../input/' + name, 'w+')

f.write(str(nodes) + '\n')
f.write(str(edges) + '\n')



remaining_edges -= (length + 1)

# -----------------------------------------------------------

while remaining_edges:
    edge = random.sample(xrange(nodes), 2)
    edge.sort()
    f.write(str(edge[0]) + ' ' + str(edge[1]) + '\n')
    remaining_edges -= 1

for i in range(len(steps)-1):
    f.write(str(steps[i]) + ' ' + str(steps[i+1]) + '\n')

f.close()