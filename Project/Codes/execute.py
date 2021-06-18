# python execute.py 
from Codes.graph import csv_to_dict,draw_graph
from Codes.summary import *

def execute_main() :
    e_dict = csv_to_dict()
    draw_graph(e_dict)
    create_summary()
    keywords()
