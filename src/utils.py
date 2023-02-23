import os
from tkinter import Y
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.io as pio
from matplotlib import cm


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
        
        cap_i=abs(np.trapz(current,x=time)/3600)
        

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
    
    
    return time_list,volt_list,curr_list,temp_list,cap_list,cyc_list


def plot_rough(t,v,i,temp,cap):
    
    layout1=go.Layout(
        title='Title',
        xaxis_title='Time [sec]',
        yaxis_title='Ylabel',
        legend_title='Legend title',
        font=dict(
            family='Courier New, monospace',
            size=20,
            color='black'
        )
    )
    
    layout2=go.Layout(
        #title='Title',
        xaxis_title='Cycle',
        yaxis_title='Capacity [Ah]',
        #legend_title='Legend title',
        font=dict(
            family='Courier New, monospace',
            size=20,
            color='black'
        )
    )    
    
    fig1=go.Figure()
    fig2=go.Figure(layout=layout2)
    for k in range(len(t)):
        fig1.add_trace(go.Scatter(x=t[k],y=v[k]))
        fig1.add_trace(go.Scatter(x=t[k],y=i[k]))
        #fig1.add_trace(go.Scatter(x=t[k],y=temp[k]))

    L=np.linspace(0,len(cap)-1,len(cap))
    fig2.add_trace(go.Scatter(x=L,y=cap))


    fig1.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
        'paper_bgcolor':'rgba(0,0,0,0)'}
        )
    fig1.update_xaxes(
        tickfont=dict(
            size=20
        ),
        showline=True,linewidth=2,linecolor='black',mirror=True,
        zeroline=True,zerolinewidth=2,zerolinecolor='black',
        showgrid=True,gridwidth=1,gridcolor='black',
        ticks='outside',tickwidth=1,tickcolor='black',ticklen=10,
        minor_griddash='solid',minor_gridwidth=0.5
        #minor_ticks='inside',minortickwidth=1,minortickcolor='black',minorticklen=5
        )
    fig1.update_yaxes(
        tickfont=dict(
            size=20
        ),
        showline=True,linewidth=3,linecolor='black',mirror=True,
        zeroline=True,zerolinewidth=2,zerolinecolor='black',
        showgrid=True,gridwidth=1,gridcolor='black',
        ticks='outside',tickwidth=1,tickcolor='black',ticklen=10
        #minor_ticks='inside',minortickwidth=1,minortickcolor='black',minorticklen=5
        )
    fig2.update_layout({'plot_bgcolor':'rgba(0,0,0,0)',
        'paper_bgcolor':'rgba(0,0,0,0)'}
        )
    fig2.update_xaxes(
        tickfont=dict(
            size=20
        ),
        showline=True,linewidth=2,linecolor='black',mirror=True,
        zeroline=True,zerolinewidth=2,zerolinecolor='black',
        showgrid=True,gridwidth=1,gridcolor='black',
        ticks='outside',tickwidth=1,tickcolor='black',ticklen=10,
        minor_griddash='solid',minor_gridwidth=0.5
        #minor_ticks='inside',minortickwidth=1,minortickcolor='black',minorticklen=5
        )
    fig2.update_yaxes(
        tickfont=dict(
            size=20
        ),
        showline=True,linewidth=3,linecolor='black',mirror=True,
        zeroline=True,zerolinewidth=2,zerolinecolor='black',
        showgrid=True,gridwidth=1,gridcolor='black',
        ticks='outside',tickwidth=1,tickcolor='black',ticklen=10
        #minor_ticks='inside',minortickwidth=1,minortickcolor='black',minorticklen=5
        )
    
    
    
    fig1.show()
    fig2.show()
    
    
def plot_3d(v,i,t,T,path2):
    

    cycles=np.linspace(0,len(t)-1,len(t))

    y_total=[]
    for j in range(len(t)):
        y1=np.ones((len(t[j]),))*j
        if j==0:
            y_total=[y1]
        else:
            y_total=y_total+[y1]



    fig=go.Figure()
    for cycle in range(len(cycles)):
        
        x=np.array(t[cycle])
        #y=np.ones((len(x),))*cycle
        y=np.array(y_total[cycle])
        z1=np.array(v[cycle])
        z2=np.array(i[cycle])
        z3=np.array(T[cycle])
        
        fig.add_trace(
            go.Scatter3d(x=x,y=y,z=z1,mode='lines',marker=dict(color='#0000FF'))
        )
        fig.add_trace(
            go.Scatter3d(x=x,y=y,z=z2,mode='lines',marker=dict(color='#FF0000'))
        )
        fig.add_trace(
            go.Scatter3d(x=x,y=y,z=z3,mode='lines',marker=dict(color='#00FF00'))
        )        
      

    fig.update_xaxes(
    tickfont=dict(
        size=20
    ),
    showline=True,linewidth=2,linecolor='black',mirror=True,
    zeroline=True,zerolinewidth=2,zerolinecolor='black',
    showgrid=True,gridwidth=1,gridcolor='black',
    ticks='outside',tickwidth=1,tickcolor='black',ticklen=10,
    minor_griddash='solid',minor_gridwidth=0.5
    #minor_ticks='inside',minortickwidth=1,minortickcolor='black',minorticklen=5
    )
    fig.update_layout(
        title_text='3d'
    )
    pio.write_image(fig,path2+'3d_plot.png')
    




def cluster(t,v,i,T,cap,path2):
    
    #colors=cm.viridis(np.linspace(0,1,len(v)))
    
    cycles=np.linspace(0,len(t)-1,len(t))

    y_total=[]
    for j in range(len(t)):
        y1=np.ones((len(t[j]),))*j
        if j==0:
            y_total=[y1]
        else:
            y_total=y_total+[y1]


    d=pd.DataFrame()
        
    
    for k in range(len(v)):
        hist_v=np.histogram(v[k],bins=20)
        fig.add_trace(go.Scatter(x=hist_v[1][1:],y=hist_v[0],color=colors))
    pio.write_image(fig,path2+'hist_v.png')
    fig.write_html(path2+'hist_v.html')
    
    return v
