import networkx as nx
import pandas as pd
import json
import random

G = nx.read_gml('graph_with_features.gml')
path_data = pd.read_csv('data_by_index.tsv', sep='\t', header=None)

sum_correct = 0
for idx, row in path_data.iterrows():
	path = json.loads(row[0])
	node_before_target = path[-1]
	node_name = list(G.nodes)[node_before_target]
	num_neighbors = len(list(G.neighbors(node_name)))
	if num_neighbors > 0 and random.random() < (1.0 / num_neighbors):
		sum_correct += 1
print(sum_correct / len(path_data))
