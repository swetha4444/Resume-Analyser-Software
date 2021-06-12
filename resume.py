import re
import docx2txt
import networkx as nx
import matplotlib.pyplot as plt

file_name_1 = 'Mathew Elliot.docx'


def extract_programming_languages(file_name):
    # read in word file
    result = docx2txt.process(file_name)
    programming_languages_pattern = re.search(r'Programming Languages:[A-Za-z,\s0-9]*\.',result)
    programming_languages_line = programming_languages_pattern.group(0)
    languages = re.sub("Programming Languages: ","", programming_languages_line)
    languages = re.sub("\.","",languages)
    languages_clean = languages.split(', ')
    print(languages_clean)
    return languages_clean

name_1 = file_name_1.split('.')[0]
languages_mathew = extract_programming_languages(file_name_1)


names = [name_1]
def draw_graph(e_dict):
    # create a directed-graph from a dataframe
    G=nx.from_dict_of_lists(e_dict,create_using=nx.MultiDiGraph())
    plt.figure(figsize=(12,12))
    
    pos = nx.spring_layout(G)
    nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos, node_size = 4500, font_size = 18)
    plt.show()

edge_dict = {}
edge_dict[names[0]] = languages_mathew
draw_graph(edge_dict)