import numpy as np
import plotly.graph_objs as go


class MeshViewer:
    def __init__(self):
        self.data = []

    def add_mesh(self, V, F=None, **kwargs):
        mesh = go.Mesh3d(
            x=V[:,0],
            y=V[:,1],
            z=V[:,2],
            # i, j and k give the vertices of triangles
            i = F[:,0] if F is not None else None,
            j = F[:,1] if F is not None else None,
            k = F[:,2] if F is not None else None,
            showscale=False,
        )
        self.data.append(mesh)

    # set_layout to view the correct T-pose
    def show(self, clear=True, **kwargs):
        layout = go.Layout(
            margin=dict(l=20, r=20, t=20, b=20),
            width=400,
            height=400,
            scene = dict(
                xaxis = dict(title='x'),
                yaxis = dict(title='y'),
                zaxis = dict(title='z'),
            aspectmode='data', # preserve proportion of axis range
            camera= dict(
            up=dict(x=0, y=0, z=1), # z axis up
            # up=dict(x=0, y=1, z=0), # y axis up
            center=dict(x=0, y=0, z=0),
            eye=dict(x=2, y=2, z=2) # zoom in (<1) or out (>1)
        ))
        )
        fig = go.Figure(data=self.data, layout=layout)
        fig.show()
        if clear:
            self.data = []
