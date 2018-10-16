def plot(learner):
    import plotly.graph_objs as go
    from plotly.offline import iplot
    vertices = learner.tri.vertices
    Xn, Yn, Zn = zip(*vertices)
    Xe = []
    Ye = []
    Ze = []
    import itertools
    for simplex in learner.tri.simplices:
        for s in itertools.combinations(simplex, 2):
            Xe += [vertices[i][0] for i in s] + [None]
            Ye += [vertices[i][1] for i in s] + [None]  
            Ze += [vertices[i][2] for i in s] + [None]
    colors = [learner.data[p] for p in learner.tri.vertices]



    trace1 = go.Scatter3d(x=Xe, y=Ye, z=Ze, mode='lines', 
        line=dict(color='rgb(125,125,125)', width=1), hoverinfo='none')
    marker = dict(symbol='circle', size=3, color=colors, colorscale='Viridis',
                  line=dict(color='rgb(50,50,50)', width=0.5))
    trace2 = go.Scatter3d(x=Xn, y=Yn, z=Zn, mode='markers',
                          name='actors', marker=marker,
                          hoverinfo='text' )

    axis = dict(showbackground=False,
                showline=False,
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                title=''
                )

    layout = go.Layout(
        title="Triangulation of LearnerND",
        showlegend=False,
        scene=dict(
            xaxis=dict(axis),
            yaxis=dict(axis),
            zaxis=dict(axis),
        ),
        margin=dict(
            t=100
        ),
        hovermode='closest')

    data=[trace1, trace2]
    fig=go.Figure(data=data, layout=layout)

    return iplot(fig)
