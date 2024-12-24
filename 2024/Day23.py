from itertools import combinations
with open("input.in", "r") as f:
    lines = f.read().splitlines()

graph = {}  # Name: Connections
for link in lines:
    c1 = link.split("-")[0]
    c2 = link.split("-")[1]
    if c1 not in graph:
        graph[c1] = []
    if c2 not in graph:
        graph[c2] = []
    graph[c1].append(c2)
    graph[c2].append(c1)


def bron_kerbosch(r, p, x, graph, largest_clique):
    """
    Bron-Kerbosch algorithm to find maximal cliques.

    Args:
        r: Current clique being built.
        p: Potential nodes to be added to the clique.
        x: Nodes already processed (excluded).
        graph: The graph represented as an adjacency list.
        largest_clique: Stores the largest clique found so far.
    """
    if not p and not x:
        if len(r) > len(largest_clique):
            largest_clique[:] = r  # Update largest_clique in place
        return

    for v in p[:]:  # Iterate over a copy to allow modification of p
        new_r = r + [v]
        new_p = [node for node in p if node in graph[v]]
        new_x = [node for node in x if node in graph[v]]
        bron_kerbosch(new_r, new_p, new_x, graph, largest_clique)
        p.remove(v)
        x.append(v)


largest_clique_found = []
bron_kerbosch([], list(graph.keys()), [], graph, largest_clique_found)
password = ",".join(sorted(largest_clique_found))

print(password)
