import pandas as pd
import csv

# create cleaned up paths (list of article names)
paths = pd.read_csv("data_from_snap/paths_finished.tsv", sep="\t", header=None, skiprows=16)
paths = list(paths[3])
newPaths = []
for pathStr in paths:
	articles = pathStr.split(";")
	while ("<" in articles):
		index = articles.index("<")
		articles = articles[:index-1] + articles[index+1:]
	if len(articles) <= 33:
		newPaths.append(articles)

with open("paths_cleaned.tsv", "w") as f:
    wr = csv.writer(f, delimiter="\t")
    wr.writerows(newPaths)


# create data and labels
paths = []
with open("paths_cleaned.tsv", "r") as f:
	wr = csv.reader(f, delimiter="\t")
	for row in wr:
		paths.append(row)


articles = pd.read_csv("data_from_snap/articles.tsv", sep="\t", header=None)

memo = {}
def getIndex(article):
	if article in memo:
		return memo[article]
	index = articles.loc[articles[0] == article].index[0]
	memo[article] = index
	return index

newPaths = []
for path in paths:
	for i in range(len(path)):
		path[i] = getIndex(path[i])
	newPaths.append(path)

finalPaths = []
for path in newPaths:
	finalPath = []
	for _ in range(33 - len(path)):
		finalPath.append(-1)
	for articleIdx in path:
		finalPath.append(articleIdx)
	finalPaths.append(finalPath)

finalData = []
for indexPath in finalPaths:
	data = indexPath[:32]
	target = indexPath[-1]
	finalData.append((data, target))

with open("data_by_index.tsv", "w") as f:
    wr = csv.writer(f, delimiter="\t")
    wr.writerows(finalData)


