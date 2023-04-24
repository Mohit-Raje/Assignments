def a_star(start , goal):
    open_set={start}
    closed_set=set()
    g_score={start : 0}
    parents={start : start}

    while open_set:
        current = min(open_set , key=lambda x : g_score[x] + heuristic(x))
        if current == goal or Graph_nodes[current] is None:
            path=[]

            while current != start:
                path.append(current)
                current=parents[current]
            path.append(start)
            path.reverse()
            return path
    
        open_set.remove(current)
        closed_set.add(current)

        for neighbour , cost in Graph_nodes[current]:
            tent_g_score= g_score[current] + cost

            if neighbour in closed_set :
                continue
            if neighbour not in open_set or tent_g_score < g_score[neighbour]:
                parents[neighbour]=current 
                g_score[neighbour]=tent_g_score

                if neighbour not in open_set:
                    open_set.add(neighbour)
    return None

def heuristic(node):
    h_dist={'A':11 , 'B':6 , 'C':99 , 'D':1 , 'E': 7  ,'G':0}
    return h_dist[node]

Graph_nodes = {
    'A':[ ('B' , 2) , ('E' , 3)],
    'B' : [('C' , 1) , ('G' , 9)],
    'C' : None,
    'E': [('D' , 6)],
    'D' : [('G' , 1)]

}
print(a_star('A' ,'G'))

# Oputput : ['A', 'E', 'D', 'G']

                
