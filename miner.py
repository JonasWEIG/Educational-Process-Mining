# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:21:51 2021

@author: ba42pizo
"""

import pandas as pd
import pm4py

'''
def import_csv(file_path):
    event_log = pandas.read_csv(file_path, sep=';')
    event_log = pm4py.format_dataframe(event_log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))
    
'''

file_path = r'C:\Users\ba42pizo\Desktop\python\WiSe 21\test.csv'
log = pm4py.format_dataframe(pd.read_csv(file_path, sep=';'), case_id='case_id',
activity_key='activity',timestamp_key='timestamp')
#log = log[log['@@index']< 40]
process_tree = pm4py.discover_tree_inductive(log)
bpmn_model = pm4py.convert_to_bpmn(process_tree)
pm4py.view_bpmn(bpmn_model)

from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.visualization.process_tree import visualizer as pt_visualizer

tree = inductive_miner.apply_tree(log)

gviz = pt_visualizer.apply(tree)
pt_visualizer.view(gviz)