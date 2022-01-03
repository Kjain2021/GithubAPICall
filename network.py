from pyvis.network import Network
import networkx as nx
from IPython.core.display import display, HTML
from script import repos_df

nt = Network('100%', '100%', bgcolor='#222222', font_color='white')

G = nx.Graph()
G.add_node('Interview-practice')

for _, row in repos_df.iterrows():
    node_name = row['Full name']
    G.add_node(node_name)
    G.add_edge('Interview-practice', node_name)




nt.from_nx(G)
nt.repulsion() 
nt.show('index.html')

