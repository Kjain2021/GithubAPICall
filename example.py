from pyvis import network as net
from IPython.core.display import display, HTML
g=net.Network(height='100%', width='100%',heading='testing')
g.add_node(1)
g.add_node(2)

g.show('index.html')
display(HTML('index.html'))
