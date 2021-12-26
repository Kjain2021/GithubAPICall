from collections import Counter


topics_list = [i['Topics'] for i in repo_list_filtered]
topics_list_flatten = [item for sublist in topics_list for item in sublist]
topics_counter = Counter(topics_list_flatten)
topics_counter = Counter(el for el in topics_counter.elements() if topics_counter[el] >= 2)

nodes = []
edges = []

for k,v in topics_counter.most_common():
    node = {"Id": k,
            "Size": v*1000,
            "Type": "topic",
            "Label": k
            }
    nodes.append(node)
print(len(nodes))

for record in repo_list_filtered:
    node = {"Id": record['Full name'],
            "Size": record['Number of stars'],
            "Type": "repo",
            "Label": record['Full name']
            }
    nodes.append(node)
    
    for topic in record['Topics']:
        if topic in topics_counter:
            edge = {"Source": record['Full name'],
                    "Target": topic}
            edges.append(edge)

print(len(nodes))
print(len(edges))