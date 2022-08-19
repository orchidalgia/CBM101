scl = 80 # scaling factor for plotting

# we have to pass in a list of the 
d = dict(G.degree)

nl = list(d.keys()) #only the nodes
print(nl)

sz = [v*scl for v in d.values()] #only their degree (scaled up)
print(sz)

# now we have successfully split them into 2, with matching order
nx.draw(G, nodelist=nl, node_size=sz, with_labels=True)
