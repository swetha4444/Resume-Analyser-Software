# python execute.py 
from graph import csv_to_dict,draw_graph
from summary import *

def execute_main() :
    e_dict = csv_to_dict()
    draw_graph(e_dict)
    create_summary()
    keywords()