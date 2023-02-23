import json
import numpy as np
import os
import utils
import plotly.express as px
import plotly.graph_objects as go
import new_utils


path='/mnt/ysk/datafolder/nasa_battery_json/'
path2='/mnt/ysk/20221020/image/'

with open(path+'./B0005_charge.json') as f:
    charge_data1=json.load(f)
    
with open(path+'./B0005_discharge.json') as f:
    discharge_data1=json.load(f)

test=px.data.medals_long()

t1,v1,i1,temp1,cap1,cyc_list1=new_utils.dataset(discharge_data1)


# d={'volt':v,'cycle':cyc,'dqdv':dqdv_list,'time':t,'cap':cap}

new_utils.plot_data(t1,v1,i1,temp1,cap1,cyc_list1,path2,'time','volt')
new_utils.plot_data(t1,v1,i1,temp1,cap1,cyc_list1,path2,'time','curr')
new_utils.plot_data(t1,v1,i1,temp1,cap1,cyc_list1,path2,'time','temp')

new_utils.dqdv(t1,v1,i1,temp1,cap1,cyc_list1,path2,'volt','dqdv')
new_utils.dqdv(t1,v1,i1,temp1,cap1,cyc_list1,path2,'temp','dqdv')




