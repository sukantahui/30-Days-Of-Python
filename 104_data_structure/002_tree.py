
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(210,210,210)', width=1),
                   hoverinfo='none'
                   ))
fig.add_trace(go.Scatter(x=Xn, mode='markers',  name='bla', marker=dict(symbol='circle-dot', size=18,color='#6175c1',    #'#DB4551', line=dict(color='rgb(50,50,50)', width=1)),
                  text=labels,
                  hoverinfo='text',
                  opacity=0.8
                  ))







