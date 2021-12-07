import networkx as nx
import pandas as pd
import json

G = nx.read_gml("data_from_paper/graph.gml")
nodes = pd.read_csv("data_from_snap/articles.tsv", sep="\t", header=None)
cat_embeds = pd.read_csv("category_embeddings.tsv", sep="\t", header=None)
article_embeds = pd.read_csv('data_from_paper/article_embeddings.txt', sep=" ", header=None).iloc[: , :-1]

new_node_features = {}
with open("data_from_paper/nodes.txt") as file:
	# nodes.txt reads (node_id, out_degree, in_degree)
	# edges.txt reads (edge_id, src_node_id, dst_node_id, tf_idf, num_link_clicked)
	for line in file:
		line = line.strip().split("\t")
		node_id, out_degree, in_degree = int(line[0]), float(line[1]), float(line[2])
		node_label = nodes.iloc[node_id][0]
		cat_embedding = json.loads(cat_embeds.loc[cat_embeds[0] == node_label][1].item())
		art_embed = article_embeds.iloc[node_id].to_list()
		new_node_features[node_label] = { "out_degree": out_degree, "in_degree": in_degree, "category_multi_hot": cat_embedding, "article_embed": art_embed }
		if "category0" in G.nodes[node_label]:
			del G.nodes[node_label]["category0"]
		if "category1" in G.nodes[node_label]:
			del G.nodes[node_label]["category1"]
		if "category2" in G.nodes[node_label]:
			del G.nodes[node_label]["category2"]
		if "category3" in G.nodes[node_label]:
			del G.nodes[node_label]["category3"]
		keys_to_remove = [x for x in G.nodes[node_label].keys() if x.startswith("path")]
		for key in keys_to_remove:
			del G.nodes[node_label][key]
nx.set_node_attributes(G, new_node_features)

# new_edge_features = {}
# with open("data_from_paper/edges.txt") as file:
# 	for line in file:
# 		line = line.strip().split("\t")
# 		src_node_id, dst_node_id, tf_idf, num_link_clicked = int(line[1]), int(line[2]), float(line[3]), float(line[4])
# 		src_node_label, dst_node_label = nodes.iloc[src_node_id][0], nodes.iloc[dst_node_id][0]
# 		new_edge_features[(src_node_label, dst_node_label)] = { "tf_idf": tf_idf, "num_link_clicked": num_link_clicked }
# 		del G.edges[(src_node_label, dst_node_label)]['weight']
# nx.set_edge_attributes(G, new_edge_features)

nx.write_gml(G, "graph_with_features.gml")
