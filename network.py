
from pyvis.network import Network
import networkx as nx
from IPython.core.display import display, HTML
from script import repos_df

nt = Network('100%', '100%', bgcolor='#222222', font_color='white')

G = nx.Graph()
G.add_node('Interview-practice')



for _, row  in repos_df.iterrows():
         node_name = row['Full name']
         if (row['Language'] == "Python" ):
             G.add_node(node_name, color='red')
             G.add_edge('Interview-practice', node_name)
         if(row['Language'] == "Java"):
             G.add_node(node_name,  color='green')
             G.add_edge('Interview-practice', node_name)
         if(row['Language'] == "JavaScript"):
             G.add_node(node_name,  color='pink')
             G.add_edge('Interview-practice', node_name)
         if(row['Language'] == "C++"):
             G.add_node(node_name, color='yellow')
             G.add_edge('Interview-practice', node_name)
         if(row['Language'] == "HTML"):
             G.add_node(node_name, color='purple')
             G.add_edge('Interview-practice', node_name)
            

         else:
             G.add_node(node_name)
             G.add_edge('Interview-practice', node_name)




nt.from_nx(G)
nt.repulsion() 
nt.show('index.html')

