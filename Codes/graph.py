import re
import docx2txt
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def csv_to_dict():
    names = []
    edge_dict = {}
    data = pd.read_csv("data.csv") 
    for i in range(len(data)):
        print(data["skills"][i])
        skills = data["skills"][i].split(", ")
        edge_dict[data["name"][i]] = skills
    return edge_dict

def draw_graph(e_dict):
    # create a directed-graph from a dataframe
    G=nx.from_dict_of_lists(e_dict,create_using=nx.MultiDiGraph())
    plt.figure(figsize=(12,12))
    pos = nx.spring_layout(G)
    nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos, node_size = 4500, font_size = 18)
    plt.savefig('knowledge.png')
    plt.show()

e_dict = csv_to_dict()
print(e_dict)
draw_graph(e_dict)