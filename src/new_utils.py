import os
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.io as pio
from matplotlib import cm
import matplotlib
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls


def dataset(data):
    
    time_list=[]
    volt_list=[]
    curr_list=[]
    temp_list=[]
    soh_list=[]
    cyc_list=[]
    cycle0=list(data.keys())[0]
    
    
    t0=data[cycle0]['time']
    i0=data[cycle0]['current_battery']
    
    cap0=np.trapz(i0,x=t0)/3600
    cap_list=[]
    
    cnt=0
    for cycle in data.keys():
        
        time=data[cycle]['time']
        voltage=data[cycle]['voltage_battery']
        current=data[cycle]['current_battery']
        temp=data[cycle]['temp_battery']
        
        cyc=np.ones((len(time),))*cnt
        
        #print(abs(np.trapz(current,x=time)/3600))
        
        cap_i=np.zeros((len(time,)))
        
        for m in range(len(time)-1):
            cap_i_n=abs(np.trapz(current[m:m+2],x=time[m:m+2])/3600)
            cap_i[m+1]=cap_i_n
        
        

        if cnt==0:
            time_list=[time]
            volt_list=[voltage]
            curr_list=[current]
            temp_list=[temp]
            cap_list=[cap_i]
            cyc_list=[cyc]
        else:
            time_list=time_list+[time]
            volt_list=volt_list+[voltage]
            curr_list=curr_list+[current]
            temp_list=temp_list+[temp]
            cap_list=cap_list+[cap_i]
            cyc_list=cyc_list+[cyc]
            
        cnt=cnt+1
    
 


    return time_list,volt_list,curr_list,temp_list,cap_list,cyc_list



def plot_data(t,v,i,T,cap,cyc,path2,x_axis,y_axis):

    d={'volt':v,'curr':i,'temp':T,'cycle':cyc,'time':t,'cap':cap}
    df=pd.DataFrame(data=d)
    print(df)
    
    color=cm.rainbow(np.linspace(0,1,len(v)))
    #matplotlib.colors.to_hex([ 0.47, 0.0, 1.0, 0.5 ], keep_alpha=True)

    #'''

    fig=go.Figure()
    for k in range(len(v)):
        x=df[x_axis][k]
        y=df[y_axis][k]
        
        fig.add_trace(go.Scatter(
            x=x,y=y, #y=cap*hist_num=cap at volt
            mode='lines',
            marker_color=matplotlib.colors.to_hex(color[k])
        ))        
        #trace for 0-29,42 plot time 
     
    fig.show()
    #'''
    
    fig.write_image(path2+y_axis+'.eps')
    '''
    username='hlinak3014' #username
    api_key='R1nKjdkHf0bTw24iHx5C' #generate key in chart-stuio.plotly.com/settings/api
    chart_studio.tools.set_credentials_file(username=username,api_key=api_key)
    py.plot(fig,filename='data',auto_open=False)
    '''

    
def dqdv(t,v,i,T,cap,cyc,path2,x_axis,y_axis):

    dvdt_list=[]
    dqdt_list=[]
    dqdv_list=[]
    dq_list=[]

    for k in range(len(v)):
        
        dv=np.diff(np.asarray(v[k]),n=1)
        dq=np.diff(np.asarray(cap[k]),n=1)
        dt=np.diff(np.asarray(t[k]),n=1)
        dvdt=dv/dt
        dqdt=dq/dt
        dqdv=list(abs(dqdt/dvdt))
        
        q=np.trapz(dqdv,v[k][:-1])
        
        #dq=np.trapz(dqdv,x=dv)
        #dq=list(dq)
        #dtdv=dt/dv
        #dqdv=list(dtdv*dqdt)

        if k==0:
            dvdt_list=[dvdt]
            dqdt_list=[dvdt]
            dqdv_list=[dqdv]
            q_list=[q]

        else:
            dvdt_list=dvdt_list+[dvdt]
            dqdt_list=dqdt_list+[dqdt]
            dqdv_list=dqdv_list+[dqdv]
            q_list=q_list+[q]
    d={'volt':v,'curr':i,'temp':T,'dqdv':dqdv_list,'cycle':cyc,'time':t,'cap':cap}        
    df=pd.DataFrame(data=d)
    print(df)
    
    color=cm.rainbow(np.linspace(0,1,len(v)))
    matplotlib.colors.to_hex([ 0.47, 0.0, 1.0, 0.5 ], keep_alpha=True)

    #'''
    #time vs volt plot
    bins=17 #volt points 2.7~4.3 in 17points
    x_new=np.linspace(2.7,4.3,bins)

    fig=go.Figure()
    for k in range(len(v)):
        x=df['volt'][k]
        y=df['cap'][k]
        hist_q=np.histogram(x,bins=x_new)
        y=np.mean(y) #average value of capacity
        
        fig.add_trace(go.Scatter(
            x=x_new,y=y*hist_q[0], #y=cap*hist_num=cap at volt
            mode='lines',
            marker_color=matplotlib.colors.to_hex(color[k])
        ))        
        #trace for 0-29,42 plot time 
     
    fig.show()
    #'''
    
    fig.write_image(path2+'figure/Z'+'.eps')
    
    username='hlinak3014' #username
    api_key='R1nKjdkHf0bTw24iHx5C' #generate key in chart-stuio.plotly.com/settings/api
    chart_studio.tools.set_credentials_file(username=username,api_key=api_key)
    py.plot(fig,filename='dqdv',auto_open=False)
